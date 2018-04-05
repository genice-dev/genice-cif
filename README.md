# genice-cif

A [GenIce](https://github.com/vitroid/GenIce) plugin to import CIF file.

## Requirements

    % make prepare
will install required packages via pip.

* [GenIce](https://github.com/vitroid/GenIce) >=0.16.
* [cif2ice](https://github.com/vitroid/cif2ice) >=0.2.

## Installation

### System-wide installation

Not supported.

### Private installation

    % make install
or copy the files in lattices into your local lattices folder of GenIce.

## Usage

	% genice zeolite[ITT] > ITT.gro
to obtain zeolite structure from [Zeolite DB](http://www.iza-structure.org/IZA-SC).

	% genice cif[RHO.cif] > RHO.gro
to convert local cif file to Gromacs format.

## Test in place

    % make test
