"""Nox sessions for the Jupyter Surveys documentation."""

import nox

nox.options.default_venv_backend = "uv|virtualenv"


@nox.session(name="docs")
def docs(session):
    """Build the documentation as static HTML."""
    session.chdir("docs")
    session.install("mystmd")
    session.run("myst", "build", "--html")


@nox.session(name="docs-live")
def docs_live(session):
    """Start a live development server for the documentation."""
    session.chdir("docs")
    session.install("mystmd")
    session.run("myst", "start")
