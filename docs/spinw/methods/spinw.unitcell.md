(spinw-unitcell)=

# spinw.unitcell method

## Syntax
  
`cellInfo = unitcell(obj, idx)`
  
## Description
  
`cellInfo = unitcell(obj, idx)` returns information on symmetry
inequivalent atoms and allowing to subselect certain atoms using the
`idx` index vector.
  
## Examples
  
The example keeps only the first and third symmetry inequivalent atoms in
`cryst` object.
```matlab
cryst.unit_cell = unitcell(cryst,[1 3]);
```
The example keeps only the atoms with labels `'O'` (Oxygen) atoms in
`cryst` object.
```matlab
cryst.unit_cell = unitcell(cryst,'O');
```
  
## Input Arguments
  
`obj`
: [spinw](#spinw) object.
  
`idx`
: Selects certain atoms. If undefined `unit_cell(obj)` or
     `obj.unit_cell` returns information on all atoms. The selection
     can be also done according to the atom labels, in this case
     either a string of the label or cell of strings for several
     labels can be given.
  
## Output Arguments
  
`cellInfo`
: Structure that contains all the fields of [spinw.unit_cell](#spinw-unit-cell).
  
## See Also
  
[spinw.addtwin](#spinw-addtwin) \| [spinw.twinq](#spinw-twinq) \| [spinw.unit_cell](#spinw-unit-cell)
