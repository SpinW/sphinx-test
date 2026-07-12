(swsym)=

# swsym package

```{toctree}
:maxdepth: 1
:glob:
:hidden:

sym/*
```

This package deals with symmetry operators of crystallographic space
groups. It can read the standard space group definitions stored in
[symmetry.dat](<matlab:edit(%5Bsw_rootdir,'dat_files',filesep,'symmetry.dat'%5D)>), generate all symmmetry elements, determine all symmetry
equivalent positions, etc.

All symmetry operators `symOp` are defined by a matrix with dimensions of
$[3 \times 4 \times n_{op}]$, where `symOp(1:3,1:3,:)` stores the $[3 \times
3]$ rotation matrices while the `symOp(1:3,4,:)` holds the corresponding
translation vectors.

## Files

- [swsym.add](#swsym-add) saves user defined symmetry operators
- [swsym.bond](#swsym-bond) generates all symmetry equivalent bonds
- [swsym.generator](#swsym-generator) returns symmetry operators of a given space group
- [swsym.genreduce](#swsym-genreduce) reduces symmetry operators to the generators
- [swsym.isop](#swsym-isop) determines if a matrix is symmetry operator
- [swsym.operator](#swsym-operator) generates all symmetry elements from given space group
- [swsym.oporder](#swsym-oporder) determine the order of the symmetry operator
- [swsym.point](#swsym-point) determines local point group symmetry in a space group
- [swsym.position](#swsym-position) generates symmetry equivalent positions
- [swsym.str](#swsym-str) generates a string equivalent of symmetry operators
