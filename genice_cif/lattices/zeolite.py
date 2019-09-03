#!/usr/bin/env python3
"""
A loader plugin for GenIce to read CIF file or to obtain structures in Zeolite DB.

* To convert a local cif file to Gromacs format,

	% genice cif[RHO.cif] > RHO.gro

* Some zeolites share the network topology with low-density ices. If you want to retrieve a zeolite ITT structure from [IZA structure database](http://www.iza-structure.org/databases) to prepare a low-density ice, try the following command:

	% genice zeolite[ITT] > ITT.gro
"""

desc = { "ref": {},
         "brief": "Read a CIF file.",
         "usage": __doc__
        }

if __name__[-16:] == "lattices.zeolite":
    desc["brief"] = "Obtain from IZA Zeolite DB."


#system modules
import os
import sys
import itertools as it
import logging
#external modules
import numpy as np
from requests import get #requests package
import validators        #validators package
from cif2ice import read_cif
from genice.cell import cellvectors

def shortest_distance(atoms,cell):
    Lmin = 1e99
    for a1,a2 in it.combinations(atoms@cell,2):
        d = a1-a2
        L = d@d
        if L < Lmin:
            Lmin = L
    return Lmin**0.5


def is_unique(L, pos):
    for x in L:
        d = x-pos
        d -= np.floor(d + 0.5)
        if np.dot(d,d) < 0.0000001:
            return False
    return True


def genice_lattice(atoms, cellshape, matchfunc=None):
    global cell, celltype, waters, coord, density
    logger = logging.getLogger()
    filtered = []
    if matchfunc is not None:
        for a in atoms:
            if matchfunc(a[0]):
                filtered.append(a[1:])
        atoms = np.array(filtered)
    else:
        atoms = np.array([a[1:] for a in atoms])
    logger.debug("Atoms: {0}".format(atoms))
    cell = cellvectors(*cellshape)
    dmin = shortest_distance(atoms, cell)
    scale = 2.76 / dmin
    logger.debug("Shape: {0}".format(cellshape))
    logger.debug("Scale: {0}".format(scale))
    volume = np.linalg.det(cell)
    icell  = np.linalg.inv(cell)
#    uniques = []
#    for name,x,y,z in atoms:
#        rpos = np.dot([x,y,z], icell)
#        rpos -= np.floor(rpos)
#        #Do twice to reduce the floating point uncertainty.
#        #(Hint: assume the case when x=-1e-33.)
#        rpos -= np.floor(rpos)
#        if is_unique(uniques, rpos):
#            uniques.append(rpos)
#    waters = uniques

    waters = atoms
    coord = "relative"
    # bondlen = 3
    density = len(atoms)*18.0/(volume*scale**3*1e-24*6.022e23)

    
def download(url, file_name):
    # open in binary mode
    with open(file_name, "wb") as file:
        # get request
        response = get(url)
        # write to file
        file.write(response.content)
        
def argparser(arg):
    logger = logging.getLogger()
    args = arg.split(":")
    name = args[0]
    logger.info(name)
    #input must be a file......too bad.
    if os.path.exists(name):
        fNameIn = name
    else:
        if validators.url(name):
            URL = name
            name = os.path.basename(name)
            if name[-4:] in (".cif", ".CIF"):
                name = name[:-4]
        elif __name__[-16:] == "lattices.zeolite":
            # it only works when my module name is zeolite.
            URL = "http://www.iza-structure.org/IZA-SC/cif/"+name+".cif"
        fNameIn = name + ".cif"
        assert validators.url(URL)
        download(URL, fNameIn)
    logger.info("Input: {0}".format(fNameIn))
    atoms, cellshape = read_cif.read_and_process(fNameIn, make_rect_box=False)
    genice_lattice(atoms, cellshape, matchfunc=lambda x: x[0] != "O")


        
# Do nothing by default; it causes an error when arguments are missing.
