"""MkDocs hooks — run presentation build before each site build."""

import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location(
    "build_presentations",
    Path(__file__).with_name("build_presentations.py"),
)
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)
_build_presentations = _mod.main


def on_pre_build(**kwargs):
    _build_presentations()
