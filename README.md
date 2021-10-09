# sphinx-remove-toctree

Improve your Sphinx build time by selectively removing TocTree objects from pages.
This is useful if your documentation has some pages with **a lot** of children.
For example, generated API documentation.

In this case, the API documentation will have thousands of stub pages that
drastically slown down your build. This extension can be used to remove the
sidebar links for just the pages you specify, so can speed up the build.

## Usage

To use this extension, you provide a list of paths to pages for which their toctrees should be removed from documentation at build time.
This means that those pages will still be in your site, but their children won't show up in your site's **navigation bar**.

- **Install the extension**

  ```console
  $ pip install git+https://github.com/executablebooks/sphinx-remove-toctree
  ```

- **Add to extensions**

  ```python
  extensions = ["sphinx_remove_toctree"]
  ```

- **Define the pages to suppress toctrees in sidebar**

  Use paths relative to your documentation root. These pages will **not** have
  their children show up in the sidebar.

  ```python
  remove_toctrees_from = ["path/to/page1.md", "page_two.rst"]
  ```

  optionally, you can also use `glob` patterns, like so:

  ```python
  remove_toctrees_from = ["reference/*.md"]
  ```

## Try it with this documentation

This extension doesn't have a hosted documentation page, but there is one in the `docs/` folder of this repository.
You can use that folder to preview this extension in action.
