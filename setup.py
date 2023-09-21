#!/usr/bin/env python

# from distutils.core import setup, Extension
from setuptools import setup, Extension
import os
import codecs
import re

#Copied from wheel package
here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(os.path.dirname(__file__), 'genice2_cif', '__init__.py'),
                 encoding='utf8') as version_file:
    metadata = dict(re.findall(r"""__([a-z]+)__ = "([^"]+)""", version_file.read()))



long_desc = "".join(open("README.md").readlines())


setup(
    name='genice2-cif',
    version=metadata['version'],
    description='CIF reader plugin for GenIce.',
    long_description=long_desc,
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
    ],
    author='Masakazu Matsumoto',
    author_email='vitroid@gmail.com',
    url='https://github.com/vitroid/genice-cif/',
    keywords=['genice', 'CIF'],

    packages=['genice2_cif',
              'genice2_cif.lattices',
    ],

    entry_points = {
        'genice2_lattice': [
            'cif    = genice2_cif.lattices.cif',
            'zeolite= genice2_cif.lattices.zeolite',
        ],
    },
    install_requires=['cif2ice>=0.3.0', 'GenIce2', 'validators'],

    license='MIT',
)
