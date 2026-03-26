"""Convert download source markdown files to .docx assets.

Reads markdown files from docs/activities/ that end with _download.md,
strips YAML front matter and jinja syntax, then converts to .docx
files in docs/downloads/.
"""

import re
from pathlib import Path

from md2docx.core import MD2DOCX


PROJECT_ROOT = Path(__file__).resolve().parent.parent
DOWNLOAD_SOURCES = PROJECT_ROOT / "docs" / "activities"
OUTPUT_DIR = PROJECT_ROOT / "docs" / "downloads"


def strip_front_matter(text: str) -> str:
    """Remove YAML front matter delimited by ---."""
    return re.sub(r"^---\n.*?\n---\n*", "", text, count=1, flags=re.DOTALL)


def strip_jinja(text: str) -> str:
    """Remove jinja2 template tags and blocks."""
    text = re.sub(r"\{%.*?%\}", "", text)
    text = re.sub(r"\{\{.*?\}\}", "", text)
    return text


def convert_file(source: Path, output: Path) -> None:
    """Convert a single markdown file to docx."""
    md_text = source.read_text(encoding="utf-8")
    md_text = strip_front_matter(md_text)
    md_text = strip_jinja(md_text)

    converter = MD2DOCX()
    converter.convert(
        md_text,
        output_file=str(output),
        default_font="Calibri",
        default_font_size=11,
    )
    print(f"  {source.name} -> {output.name}")


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    sources = sorted(DOWNLOAD_SOURCES.glob("activity_*.md"))
    if not sources:
        print("No activity files found.")
        return

    print(f"Converting {len(sources)} file(s):")
    for source in sources:
        stem = source.stem
        output = OUTPUT_DIR / f"{stem}.docx"
        convert_file(source, output)

    print("Done.")


if __name__ == "__main__":
    main()
