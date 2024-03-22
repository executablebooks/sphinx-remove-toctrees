import os
from pathlib import Path
from shutil import copytree

from bs4 import BeautifulSoup
from sphinx import version_info as sphinx_version_info

pytest_plugins = "sphinx.testing.fixtures"

path_test_doc = Path(__file__).parent / "site"


def test_build_html(make_app, tmp_path):
    """Test building the base html template and config."""
    src_dir = tmp_path / "test_doc"
    copytree(path_test_doc, src_dir)    

    # For compatibility with multiple versions of sphinx, convert pathlib.Path to
    # sphinx.testing.path.path here.
    if sphinx_version_info >= (7, 2):
        app_src_dir = src_dir
    else:
        from sphinx.testing.path import path

        app_src_dir = path(os.fspath(src_dir))

    app = make_app(srcdir=app_src_dir)
    app.build()
    index = tmp_path / "test_doc" / "_build" / "html" / "index.html"
    assert index.exists()
    index = BeautifulSoup(index.read_text())
    sidenav = index.select("ul.bd-sidenav")[0]

    # Grab all references to second-level links, we should *only* find the shown page
    second_level_links = sidenav.select(".toctree-l2 a")
    assert len(second_level_links) == 1
    assert second_level_links[0].attrs["href"] == "nested/nested_page_shown.html"
