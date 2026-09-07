"""Nox sessions for the Jupyter Surveys documentation."""

import nox

nox.options.default_venv_backend = "uv|virtualenv"


@nox.session(name="docs")
def docs(session):
    """Build the documentation as static HTML."""
    session.install("mystmd")
    session.run("python", "docs/build.py", "links")
    session.chdir("docs")
    session.run("myst", "build", "--html")
    session.run("python", "build.py", "redirects")


@nox.session(name="docs-live")
def docs_live(session):
    """Start a live development server for the documentation."""
    session.install("mystmd")
    session.run("python", "docs/build.py", "links")
    session.chdir("docs")
    session.run("myst", "start")
