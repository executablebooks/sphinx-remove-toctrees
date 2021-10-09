import os
from pathlib import Path

from setuptools import setup, find_packages

with open("./README.md") as ff:
    readme_text = ff.read()

# Parse version
init = Path(__file__).parent.joinpath("sphinx_remove_toctree", "__init__.py")
for line in init.read_text().split("\n"):
    if line.startswith("__version__ ="):
        break
version = line.split(" = ")[-1].strip('"')

docs_requirements = [
    "ipython",
    "sphinx-book-theme",
    "myst-parser",
]

setup(
    name="sphinx-remove-toctree",
    version=version,
    description="Reduce your documentation build size by selectively removing toctrees from pages.",
    long_description=readme_text,
    long_description_content_type="text/markdown",
    author="Executable Book Project",
    url="https://github.com/executablebooks/sphinx-remove-toctree",
    license="MIT License",
    packages=find_packages(),
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3 :: Only",
    ],
    python_requires=">=3.6",
    install_requires=["sphinx>=1.8"],
    extras_require={
        "code_style": ["pre-commit==2.12.1"],
        "docs": docs_requirements,
        "tests": docs_requirements + ["pytest",],
    },
)
