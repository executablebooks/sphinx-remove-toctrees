project = "Sphinx Remove Toctrees test"
extensions = ["sphinx_remove_toctree", "myst_parser"]
master_doc = "index"
html_theme = "sphinx_book_theme"
remove_toctrees_from = ["second/hidden_*", "second/direct_link_page.md"]
