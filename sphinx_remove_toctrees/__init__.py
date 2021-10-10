"""A small sphinx extension to add "copy" buttons to code blocks."""
from pathlib import Path
from sphinx.util import logging
from sphinx import addnodes


__version__ = "0.0.2"

logger = logging.getLogger(__name__)


def remove_toctrees(app, env):
    """Remove toctrees from pages a user provides.

    This happens at the end of the build process, so even though the toctrees
    are removed, it won't raise sphinx warnings about un-referenced pages.
    """
    patterns = app.config.remove_toctrees_from
    if isinstance(patterns, str):
        patterns = [patterns]

    # Figure out the list of patterns to remove from all toctrees
    to_remove = []
    for pattern in patterns:
        # Inputs should either be a glob pattern or a direct path so just use glob
        srcdir = Path(env.srcdir)
        for matched in srcdir.glob(pattern):
            to_remove.append(str(matched.relative_to(srcdir).with_suffix("")))

    # Loop through all tocs and remove the ones that match our pattern
    for _, tocs in env.tocs.items():
        for toctree in tocs.traverse(addnodes.toctree):
            new_entries = []
            for entry in toctree.attributes.get("entries", []):
                if entry[1] not in to_remove:
                    new_entries.append(entry)
            # If there are no more entries just remove the toctree
            if len(new_entries) == 0:
                toctree.parent.remove(toctree)
            else:
                toctree.attributes["entries"] = new_entries


def setup(app):
    app.add_config_value("remove_toctrees_from", [], "html")
    app.connect("env-updated", remove_toctrees)
    return {"parallel_read_safe": True, "parallel_write_safe": True}
