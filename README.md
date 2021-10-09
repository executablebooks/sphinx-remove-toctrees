# Remove toctrees from Sphinx pages

Improve your Sphinx build time by selectively removing TocTree objects from pages.
This is useful if your documentation uses auto-generated API documentation, which
generates **a lot** of stub pages

This extension can be used to remove the sidebar links for just the pages you specify, speed up the build considerably.

## Installation

Install the extension via `pip`:

```console
$ pip install git+https://github.com/executablebooks/sphinx-remove-toctree
```

and activate it by adding it to your Sphinx `conf.py` file:

```python
extensions = ["sphinx_remove_toctree"]
```

## Usage

In `conf.py`, provide a list of `glob`-like paths **relative to your documentation root**. Each entry should match to pages that should be removed from the sidebar.

For example, the following configuration will remove all pages from the folder `api/generated`, and the specific page `subfolder/page_two.rst`:

```python
remove_toctrees_from = ["api/generated/*", "subfolder/page_two.rst"]
```

This is particularly useful in combination with the `autosummary` directive, which tends to generate a ton of stub-pages that slows things down.

If you have the following autosummary directive in a page at `myfolder/page1.rst`:

```rst
.. autosummary: datetime.datetime
   :toctree: api_gen
```

This will generate stub-pages in a `myfolder/api_gen/` folder.
To remove each of these pages from your sidebar, you would configure this extension like so:

```python
remove_toctrees_from = ["myfolder/api_gen/*"]
```


## Try it with this documentation

This extension doesn't have a hosted documentation page, but there is one in the `docs/` folder of this repository.
You can use that folder to preview this extension in action.


## How this works

Sphinx keeps track of `toctree` objects to represent the structure of your documentation.
These exist in the Sphinx environment object, at `env.tocs`.
There are two places in the build where this is relevant here:

- Early in the build, Sphinx uses these `tocs` to ensure that files in your documentation are linked _somewhere_, and will raise warnings if it finds a file that is not in one of the `tocs`.
- Later in the build, Sphinx uses these `tocs` to build the HTML `toctree` with links to pages in your documentation. If there are many elements in `tocs`, it will take a long time to resolve all of these links!

This extension runs *after* the first step, but *before* the second step.
It removes all the `toctree` objects that you specify, so that no warnings are raised about missing files, but they are removed from the sidebar and don't slow down your build.
