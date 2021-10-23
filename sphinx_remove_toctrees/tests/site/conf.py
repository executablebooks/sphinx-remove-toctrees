project = "Sphinx Remove Toctrees test"
extensions = ["sphinx_remove_toctrees", "myst_parser"]
master_doc = "index"
html_theme = "sphinx_book_theme"
remove_from_toctrees = ["nested/nested_page_hidden.md", "nested_hidden/*"]
