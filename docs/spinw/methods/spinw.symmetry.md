(spinw-symmetry)=

# spinw.symmetry method

## Syntax
  
`sym = symmetry(obj)`
  
## Description
  
`sym = symmetry(obj)` returns `true` if equivalent couplings are
generated based on the crystal space group and all matrices (interaction,
anisotropy and g-tensor) are transformed according to the symmetry
operators. If `false`, equivalent couplings are generated based on bond
length, equivalent matrices won't be transformed (all identical).
   
To switch between the two behaviour use [spinw.gencoupling](#spinw-gencoupling) with the
`forceNoSym` parameter set to `true`. To remove all symmetry operators
use [spinw.nosym](#spinw-nosym).
  
## See Also
  
[spinw](#spinw) \| [spinw.nosym](#spinw-nosym) \| [spinw.gencoupling](#spinw-gencoupling)
