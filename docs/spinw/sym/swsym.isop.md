(swsym-isop)=

# swsym.isop

## Syntax
  
`result = swsym.isop(op)`
  
## Description
  
`result = swsym.isop(op)` determines whether the given matrix has
dimensions that is compatible with the size requirements of space group
operators. The given `op` matrix has to have dimensions of $$[3\times
4\times n_{op}]$$. The function returns `true` only if the input has these
dimensions.
 
## See Also
  
[swsym.generator](#swsym-generator) \| [swsym.operator](#swsym-operator)
