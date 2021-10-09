"""A small sphinx extension to add "copy" buttons to code blocks."""
from pathlib import Path
from glob import glob
from sphinx.util import logging
from sphinx import addnodes


__version__ = "0.0.1"

logger = logging.getLogger(__name__)


def remove_toctrees(app, doctree, docname):
    """Remove toctrees from pages a user provides.

    This happens at the end of the build process, so even though the toctrees
    are removed, it won't raise sphinx warnings about un-referenced pages.
    """
    pages = app.config.remove_toctrees_from
    if isinstance(pages, str):
        pages = [pages]
    for pagename in pages:
        # Inputs should either be a glob pattern or a direct path so just use glob
        srcdir = Path(app.env.srcdir)
        for match in srcdir.glob(pagename):
            match = str(match.relative_to(srcdir).with_suffix(""))
            if match not in app.env.tocs:
                logger.warning(
                    f"Found match to remove toctree, but it is not in app.env.tocs: {match}"
                )
                continue
            for toctree in app.env.tocs[match].traverse(addnodes.toctree):
                toctree.parent.remove(toctree)


def setup(app):
    app.add_config_value("remove_toctrees_from", [], "html")
    app.connect("doctree-resolved", remove_toctrees)
    return {"parallel_read_safe": True, "parallel_write_safe": True}
