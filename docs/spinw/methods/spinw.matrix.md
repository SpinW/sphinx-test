(spinw-matrix)=

# spinw.matrix property

## Sub fields
 
`mat`
: Stores the actual values of 3x3 matrices, in a matrix with
dimensions of $[3\times 3\times n_{matrix}]$, if assigned for a 
bond, the unit of energy is stored in [spinw.unit](#spinw-unit) (default value 
is meV).
 
`color`
: Color assigned for every matrix, stored in a
  matrix with dimensions of $[3\times n_{matrix}]$, with each
  column defining an RGB value.
 
`label`
: Label for every matrix, stored as string in a cell with
  dimensions of $[1\times n_{matrix}]$.
