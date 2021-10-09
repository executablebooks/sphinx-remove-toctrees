import nox
from pathlib import Path

nox.options.reuse_existing_virtualenvs = True


@nox.session()
def docs(session):
    _install_environment(session)
    session.run("sphinx-build", "-b", "html", "docs", "docs/_build/html")


@nox.session(name="tests")
def tests(session):
    _install_environment(session)
    session.run("pytest", *session.posargs)


def _install_environment(session):
    """Install the JS and Python environment needed to develop the theme."""
    # Assume that if sphinx is already installed, we don't need to re-install
    bin = Path(session.bin)
    if list(bin.rglob("spphinx-build")) and "reinstall" not in session.posargs:
        return

    session.install("-e", ".[docs,tests]")
