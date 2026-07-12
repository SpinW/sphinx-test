(spinw-fouriersym)=

# spinw.fouriersym method

## Syntax
  
`res = fouriersym(obj,Name,Value)`
  
## Description
  
`res = fouriersym(obj,Name,Value)` solves the symbolic Fourier transform
problem.
  
## Input Arguments
  
`obj`
: [spinw](#spinw) object.
  
## Name-Value Pair Arguments
  
`'hkl'`
: Symbolic definition of positions in momentum space. Default value is
  the general $Q$ point:
  ```matlab
  hkl = [sym('h') sym('k') sym('l')]
  ```
  
## See Also
  
[spinw.fourier](#spinw-fourier)
