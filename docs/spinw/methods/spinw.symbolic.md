(spinw-symbolic)=

# spinw.symbolic method

## Syntax
  
`symb = symbolic(obj)`
 
`symbolic(obj, symb)`
  
## Description
  
`symb = symbolic(obj)` returns `true` if symbolic calculation mode is on,
`false` for numeric mode.
   
`symbolic(obj, symb)` sets whether the calculations are in
symbolic/numeric (`true`/`false`) mode. Switching to symbolic mode, the
spin values, matrix elements, magnetic field, magnetic structure and
physical units are converted into symbolic variables. If this is not
desired, start with a symbolic mode from the beggining and have full
control over the values of the above mentioned variables.
  
## See Also
  
[spinw](#spinw) \| [spinw.spinwavesym](#spinw-spinwavesym)
