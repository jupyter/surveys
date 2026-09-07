#!/usr/bin/env python3
"""Prepare the MyST site and write redirects for the URLs it used to serve.

MyST builds a page slug from the file path, so a project made of ``README.md``
files gets the slugs ``readme``, ``readme-1``, ``readme-2`` and so on.  Two sets
of symlinks give every survey a slug taken from its folder name instead.  Both
are generated here and git-ignored, so adding a survey needs no extra step:

``docs/<survey>`` -> ``surveys/<survey>``
    Makes the survey folder a direct child of the MyST project, so the URL
    starts at the survey name rather than at ``surveys/<survey>``.

``surveys/<survey>/index.md`` -> ``README.md``
    MyST drops a trailing ``index`` from the URL, so the page is served at
    ``/<survey>`` rather than ``/<survey>/readme``.  The link sits next to the
    README so relative links to the data files still resolve.

Run ``links`` before ``myst build`` and ``redirects`` after it.
"""

from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
SURVEYS = ROOT / "surveys"
HTML = DOCS / "_build" / "html"

# Slugs the site served before page slugs were taken from the folder name,
# mapped to the folder each one held.  The set is closed: a survey added from
# now on never had a readme-N URL.
LEGACY_SLUGS = {
    "readme": "2015-12-notebook-ux/analysis",
    "readme-1": "2015-12-notebook-ux",
    "readme-2": "2016-05-education-survey",
    "readme-3": "2018-09-jupytercon-2018",
    "readme-4": "2020-12-jupyter-survey",
    "readme-5": "2022-08-notebooks-for-all",
    "readme-6": "2023-05-jupyterlab-accessibility",
    "readme-7": "2026-08-foundation-survey",
}

REDIRECT_PAGE = """<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <title>Redirecting to {target}</title>
    <link rel="canonical" href="{target}" />
    <meta name="robots" content="noindex" />
    <meta http-equiv="refresh" content="0; url={target}" />
  </head>
  <body>
    <p>This page moved to <a href="{target}">{target}</a>.</p>
  </body>
</html>
"""


def link(path: Path, target: str) -> None:
    """Point ``path`` at ``target``, replacing an earlier generated link."""
    if path.is_symlink():
        if os.readlink(path) == target:
            return
        path.unlink()
    elif path.exists():
        sys.exit(f"{path} already exists and is not a generated symlink")
    path.symlink_to(target)


def prune(entries) -> None:
    """Drop generated links whose target is gone, after a survey is renamed."""
    for entry in entries:
        if entry.is_symlink() and not entry.exists():
            entry.unlink()


def write_links() -> None:
    prune(sorted(DOCS.iterdir()))
    prune(sorted(SURVEYS.rglob("index.md")))
    for readme in sorted(SURVEYS.rglob("README.md")):
        link(readme.with_name("index.md"), "README.md")
    for survey in sorted(SURVEYS.iterdir()):
        if survey.is_dir() and any(survey.rglob("README.md")):
            link(DOCS / survey.name, f"../surveys/{survey.name}")
            print(f"docs/{survey.name} -> surveys/{survey.name}")


def write_redirects() -> None:
    if not HTML.is_dir():
        sys.exit(f"Nothing to add redirects to: {HTML} does not exist")
    base = os.environ.get("BASE_URL", "").rstrip("/")
    for slug, folder in LEGACY_SLUGS.items():
        if not (HTML / folder / "index.html").is_file():
            sys.exit(f"{slug} points at {folder}, which the build did not produce")
        target = f"{base}/{folder}"
        page = HTML / slug / "index.html"
        page.parent.mkdir(parents=True, exist_ok=True)
        page.write_text(REDIRECT_PAGE.format(target=target), encoding="utf-8")
        print(f"{base}/{slug} -> {target}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument(
        "command",
        choices=("links", "redirects"),
        help="links: symlink the surveys into the site; redirects: write a "
        "redirect page for each URL the site used to serve",
    )
    {"links": write_links, "redirects": write_redirects}[parser.parse_args().command]()


if __name__ == "__main__":
    main()
