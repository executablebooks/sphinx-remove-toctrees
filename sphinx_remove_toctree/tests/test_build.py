import os
from pathlib import Path
from shutil import copytree

from bs4 import BeautifulSoup
from sphinx.testing.path import path as sphinx_path
from sphinx.testing.util import SphinxTestApp

pytest_plugins = "sphinx.testing.fixtures"

path_test_doc = Path(__file__).parent / "site"


def test_build_html(make_app, tmp_path):
    """Test building the base html template and config."""
    copytree(path_test_doc, tmp_path / "test_doc")
    app = make_app(srcdir=sphinx_path(tmp_path / "test_doc"))
    app.build()
    index = tmp_path / "test_doc" / "_build" / "html" / "index.html"
    assert index.exists()
    index = BeautifulSoup(index.read_text())
    sidenav = index.select("ul.bd-sidenav")[0]

    # Grab all references to second-level links, we should *only* find the shown page
    second_level_links = sidenav.select(".toctree-l2 a")
    assert len(second_level_links) == 1
    assert second_level_links[0].attrs["href"] == "second/nested/nested_page_shown.html"
