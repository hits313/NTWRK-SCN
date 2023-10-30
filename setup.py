#! /usr/bin/env python3
from setuptools import setup

import pathlib

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

setup(
    name                =   "Ntwrk-scn",
    version             =   '1.2',
    description         =   "The Multi Purpose Web Vulnerability Scanner.",
    long_description    =   README,
    long_description_content_type = "text/markdown",
    url                 =   "https://github.com/hits313/NTWRK-SCN",
    author              =   "hits313",
    py_modules          =   ['Ntwrk-scn',],
    install_requires    =   [],
    python_requires=">=3.10",
)