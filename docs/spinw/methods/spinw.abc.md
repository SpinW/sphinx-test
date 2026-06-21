(spinw-abc)=

# spinw.abc method

## Syntax
  
`latvect = abc(obj)`
  
## Description
  
`latvect = abc(obj)` extracts the lattice vectors and angles from a
[spinw](#spinw) object.
  
## Input Arguments
  
`obj`
: [spinw](#spinw) object.
  
## Output Arguments
  
`latVect`
: Vector with elements `[a, b, c, α, β, γ]`,
  contains the lattice parameters and angles by default in Å and
  degree units respectively (see [spinw.unit](#spinw-unit) for details).
  
## See Also
  
[spinw.horace](#spinw-horace)
