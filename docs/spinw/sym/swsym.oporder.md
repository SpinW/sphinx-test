(swsym-oporder)=

# swsym.oporder

## Syntax
  
`N = swsym.oporder(symOp)`
  
## Description
  
`N = swsym.oporder(symOp)` determines the order of the `symOp` symmetry
operator, where `symOp(:,1:3)` is a rotation matrix and `symOp(:,4)` is a
translation. The value of 10 is returned if the matrix is not a valid
crystallographic symmetry operator.
  
## Examples
  
Raising any operator to the calculated order will alway return identity:
 
```matlab
O = swsym.generator('y,z,x')
```
*Output*
```
O =
     0     1     0     0
     0     0     1     0
     1     0     0     0
```
 
```matlab
R = O(:,1:3)^swsym.oporder(O)
```
*Output*
```
R =
     1     0     0
     0     1     0
     0     0     1
```
 
  
## Input Arguments
  
`symOp`
:	Symmetry operator in a matrix with dimensions of $$[3\times 4]$$.
  
## Output Arguments
 
`N`
: Integer, the order of the operator.
 
## See Also
  
[swsym.generator](#swsym-generator) \| [sw_basismat](#sw-basismat)
