#!/usr/bin/env python
from jinja2 import Template, BaseLoader, Environment, FileSystemLoader
import toml
import genice2_cif.lattices.cif
import genice2_cif.lattices.zeolite

import sys

project = toml.load("pyproject.toml")

project |= {
    "usage": genice2_cif.lattices.cif.desc["usage"],
    "version": genice2_cif.__version__,
}

t = Environment(loader=FileSystemLoader(searchpath=".")).get_template(sys.argv[1])
markdown_en = t.render(**project)
print(markdown_en)
