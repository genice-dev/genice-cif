![Logo](https://raw.githubusercontent.com/vitroid/GenIce/develop/logo/genice-v0.png)

# [genice2-cif](https://github.com/vitroid/genice-cif)

A loader plugin for [GenIce2](https://github.com/vitroid/GenIce) to read CIF file or to obtain structures in [Zeolite DB](https://www.iza-structure.org/databases/).

version 2.2.1

## Requirements

- python^3.9
- cif2ice>=0.3.0
- GenIce2^2.2.5.2
- validators\*

## Installation from PyPI

```shell
% pip install genice2-cif
```

## Usage

    A loader plugin for GenIce2 to read CIF file or to obtain structures in Zeolite DB.

    * To convert a local cif file to Gromacs format,

        % genice2 cif[RHO.cif] > RHO.gro
        % genice2 cif[ice.cif:O=O] > RHO.gro   # Specify the tetrahedral atom type ()

      * Options:

        * filename: A CIF file.
        * O=M:      Regards the atom type M as the position of a water molecule.
                    (Default is "TS" (Tetrahedral hypothetical element "T" or "S"ilica, and "O" is ignored.))

    * Some zeolites share the network topology with low-density ices. If you want to retrieve a zeolite ITT structure from [IZA structure database](http://www.iza-structure.org/databases) to prepare a low-density ice, try the following command:

        % genice2 zeolite[ITT] > ITT.gro

## Test in place

```shell
% make test
```
