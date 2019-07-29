#!/usr/bin/env python
import sys
from genice.tool import line_replacer
from genice_cif.lattices.zeolite import __doc__
import distutils.core

setup = distutils.core.run_setup("setup.py")

d = {
    "%%usage%%"   : "\n".join(__doc__.splitlines()[2:]),
    "%%version%%" : setup.get_version(),
    "%%package%%" : setup.get_name(),
    "%%url%%"     : setup.get_url(),
    "%%genice%%"  : "[GenIce](https://github.com/vitroid/GenIce)",
    "%%requires%%": "\n".join(setup.install_requires),
}


for line in sys.stdin:
    print(line_replacer(line, d), end="")
