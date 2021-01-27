# [genice2_cif](https://github.com/vitroid/genice-cif/)

A loader plugin for [GenIce2](https://github.com/vitroid/GenIce) to read CIF file or to obtain structures in Zeolite DB.

version 2.0

## Requirements


* cif2ice>=0.2.2
* GenIce2
* validators

## Installation from PyPI

```shell
% pip install genice2_cif
```

## Manual Installation

### System-wide installation

```shell
% make install
```

### Private installation

Copy the files in genice2_cif/formats/ into your local formats/ folder.

## Usage
        
    * To convert a local cif file to Gromacs format,

        % genice2 cif[RHO.cif] > RHO.gro

    * Some zeolites share the network topology with low-density ices. If you want to retrieve a zeolite ITT structure from [IZA structure database](http://www.iza-structure.org/databases) to prepare a low-density ice, try the following command:

        % genice2 zeolite[ITT] > ITT.gro

## Test in place

```shell
% make test
```
