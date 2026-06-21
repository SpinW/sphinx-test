(spinw-field)=

# spinw.field method

## Syntax
  
`field(obj,B)`
`B = field(obj)`
  
## Description
  
`field(obj,B)` sets the magnetic field stored in `obj.single_ion.field`
to `B`, where `B` is a $$[1\times 3]$$ vector.
   
`B = field(obj)` returns the current value of the magnetic field value
stored in `obj`.
   
## See Also
  
[spinw](#spinw) \| [spinw.temperature](#spinw-temperature) \| [spinw.single_ion](#spinw-single-ion)
