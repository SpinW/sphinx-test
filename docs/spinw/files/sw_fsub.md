(sw-fsub)=

# sw_fsub

## Syntax
  
`cgraph = sw_fsub(conn, next)`
  
## Description
  
`cgraph = sw_fsub(conn, next)` creates a simple graph vertex coloring,
determines non-connected sublattices for Monte-Carlo calculation.
  
## Input Arguments
  
`conn`
: Contains edge indices which are connected
  `conn(1,idx)-->conn(2,idx)` stored in a matrix with dimensions of $[2times n_{conn}]$.
  
`nExt`
: Size of the magnetic supercell in a row vector with 3 integers.
  
## Output Arguments
  
`cGraph`
: Vector, that assigns every magnetic moment to a sublattice.
  
## See Also
  
[spinw.anneal](#spinw-anneal)
