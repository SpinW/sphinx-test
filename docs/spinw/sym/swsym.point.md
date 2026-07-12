(swsym-point)=

# swsym.point

## Syntax
  
`pOp = swsym.point(symOp, r)`
  
## Description
  
`pOp = swsym.point(symOp, r)` determines the point group symmetry at a
given position in the unit cell in a given space group. It returns all the
rotation matrices of the point group.
  
## Input Arguments
  
`symOp`
: Symmetry operators of the space group stored in a matrix
  with dimensions of $[3\times 4\times n_{op}]$.
  
`r`
: Column vector with 3 elements, position in the unit cell.
  
## Output Arguments
  
`pOp`
: Point group operators in a matrix with dimensions of $[3\times 3\times
  n_{op}]$, the operators act on the relative atomic positions. To
  convert these rotation operators to Cartesian coordinate system, use:
 
  ```matlab
  R = BV*pOp(:,:,i)*inv(BV)
  ```
  where `BV` is the matrix of lattice basis vectors, see
  [spinw.basisvector](#spinw-basisvector).
  
## See Also
  
[swsym.generator](#swsym-generator) \| [swsym.operator](#swsym-operator) \| [swsym.position](#swsym-position)
