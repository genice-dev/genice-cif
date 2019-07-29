# genice-cif

A [GenIce](https://github.com/vitroid/GenIce) plugin to import CIF file.

(version 0.2)

## Requirements

    % make prepare

will install required packages via pip.

* cif2ice
* GenIce>=0.25

## Installation

### System-wide installation

Install via pip.

    % pip install genice_cif

### Private installation

Not supported.

## Usage

* To convert a local cif file to Gromacs format,

	% genice cif[RHO.cif] > RHO.gro

* Some zeolites share the network topology with low-density ices. If you want to retrieve a zeolite ITT structure from [IZA structure database](http://www.iza-structure.org/databases) to prepare a low-density ice, try the following command:

	% genice zeolite[ITT] > ITT.gro

## Test in place

    % make test
