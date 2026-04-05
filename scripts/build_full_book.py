"""Build a single DOCX file containing the full workbook.

Reads content pages in navigation order from mkdocs.yml, strips Jinja2
syntax, renders front-matter metadata inline, and converts to a single
DOCX file in docs/downloads/.
"""

import re
from pathlib import Path

import yaml
from md2docx.core import MD2DOCX

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DOCS_DIR = PROJECT_ROOT / "docs"
OUTPUT_DIR = DOCS_DIR / "downloads"
OUTPUT_FILE = OUTPUT_DIR / "teaching-for-impact-full-book.docx"

# Pages to skip (index/overview pages, presentations, offline-access)
SKIP_PAGES = {
    "presentations/index.md",
    "resources/offline-access.md",
}

# Section index pages to skip (their section heading is added separately)
SECTION_INDEX_PAGES = {
    "part-1/index.md",
    "part-2/index.md",
    "activities/index.md",
    "extra-topics/index.md",
}


def load_nav() -> list:
    """Load the nav structure from mkdocs.yml.

    Strips !!python/* tags before parsing so we can use safe_load
    on a config that contains mkdocs-specific constructors.
    """
    config_path = PROJECT_ROOT / "mkdocs.yml"
    text = config_path.read_text(encoding="utf-8")
    # Remove !!python/* YAML tags that safe_load cannot handle
    text = re.sub(r"!!python/\S+", "", text)
    config = yaml.safe_load(text)
    return config.get("nav", [])


def flatten_nav(nav, section_title=None):
    """Flatten the nested nav structure into (section_title, page_title, page_path) tuples."""
    pages = []
    for item in nav:
        if isinstance(item, str):
            pages.append((section_title, None, item))
        elif isinstance(item, dict):
            for key, value in item.items():
                if isinstance(value, str):
                    pages.append((section_title, key, value))
                elif isinstance(value, list):
                    pages.extend(flatten_nav(value, section_title=key))
    return pages


def parse_front_matter(text: str) -> tuple[dict, str]:
    """Extract YAML front matter and return (metadata, body)."""
    match = re.match(r"^---\n(.*?)\n---\n*(.*)", text, flags=re.DOTALL)
    if match:
        try:
            metadata = yaml.safe_load(match.group(1)) or {}
        except yaml.YAMLError:
            metadata = {}
        return metadata, match.group(2)
    return {}, text


def strip_jinja(text: str) -> str:
    """Remove jinja2 template tags and variable expressions."""
    text = re.sub(r"\{%.*?%\}", "", text)
    text = re.sub(r"\{\{.*?\}\}", "", text)
    return text


def render_lesson_metadata(meta: dict) -> str:
    """Render lesson front-matter metadata as markdown."""
    parts = []
    if meta.get("learning_outcomes"):
        parts.append("**Learning Outcomes**\n")
        for outcome in meta["learning_outcomes"]:
            parts.append(f"- {outcome}")
        parts.append("")
    if meta.get("guiding_questions"):
        parts.append("**Guiding Questions**\n")
        for question in meta["guiding_questions"]:
            parts.append(f"- {question}")
        parts.append("")
    return "\n".join(parts)


def render_activity_metadata(meta: dict) -> str:
    """Render activity front-matter metadata as markdown."""
    parts = []
    if meta.get("what_to_do"):
        parts.append(f"**What to do:** {meta['what_to_do']}\n")
    if meta.get("expected_output"):
        parts.append(f"**Expected output:** {meta['expected_output']}\n")
    if meta.get("approximate_time"):
        parts.append(f"**Approximate time:** {meta['approximate_time']}\n")
    if meta.get("used_in"):
        parts.append("**Used in**\n")
        for item in meta["used_in"]:
            parts.append(f"- {resolve_internal_links(item)}")
        parts.append("")
    return "\n".join(parts)


def resolve_internal_links(text: str) -> str:
    """Convert internal markdown links to plain text, keeping external URLs."""
    return re.sub(r"\[([^\]]+)\]\((?!https?://)[^)]+\)", r"\1", text)


def resolve_image_paths(text: str, page_path: str) -> str:
    """Rewrite relative image paths to absolute filesystem paths."""
    page_dir = (DOCS_DIR / page_path).parent

    def _resolve(match):
        alt, path = match.group(1), match.group(2)
        if path.startswith(("http://", "https://")):
            return match.group(0)
        resolved = (page_dir / path).resolve()
        return f"![{alt}]({resolved})"

    return re.sub(r"!\[([^\]]*)\]\(([^)]+)\)", _resolve, text)


def process_page(page_path: str) -> str:
    """Read a page, extract metadata, strip jinja, return clean markdown."""
    full_path = DOCS_DIR / page_path
    if not full_path.exists():
        print(f"  WARNING: {page_path} not found, skipping")
        return ""

    text = full_path.read_text(encoding="utf-8")
    meta, body = parse_front_matter(text)
    body = strip_jinja(body).strip()
    body = resolve_internal_links(body)
    body = resolve_image_paths(body, page_path)

    # Render metadata inline based on page type
    metadata_block = ""
    if page_path.startswith("activities/activity_"):
        metadata_block = render_activity_metadata(meta)
    elif "lesson-" in page_path:
        metadata_block = render_lesson_metadata(meta)

    if metadata_block:
        body = metadata_block + "\n" + body

    return body


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    nav = load_nav()
    pages = flatten_nav(nav)

    sections = []
    current_section = None

    for section_title, page_title, page_path in pages:
        if page_path in SKIP_PAGES or page_path in SECTION_INDEX_PAGES:
            continue

        # Add section heading when we enter a new section
        if section_title and section_title != current_section:
            current_section = section_title
            # Only add section headings for major parts (not top-level pages)
            if section_title not in ("Home", "Introduction", "Conclusion"):
                sections.append(f"# {section_title}\n")

        content = process_page(page_path)
        if content:
            # Prepend page title as a heading if available
            if page_title:
                content = f"## {page_title}\n\n{content}"
            sections.append(content)

    full_markdown = "\n\n---\n\n".join(sections)

    print(f"Converting full book to DOCX ({len(sections)} sections)...")
    converter = MD2DOCX()
    converter.convert(
        full_markdown,
        output_file=str(OUTPUT_FILE),
        default_font="Calibri",
        default_font_size=11,
    )
    print(f"  -> {OUTPUT_FILE.name}")
    print("Done.")


if __name__ == "__main__":
    main()
