(swsym-add)=

# swsym.add

## Syntax
  
`sym = swsym.add(symStr)`
 
`sym = swsym.add(symStr,symName)`
  
## Description
  
`sym = swsym.add(symStr)` saves the symmetry generators in `symStr` into
the `symmetry.dat` file and returns the line number of the space group in
the `symmetry.dat` file.
   
`sym = swsym.add(symStr,symName)` also assigns a label `symName` to the
new symmetry operators (space group).
 
## Input Arguments
  
`symStr`
: String, that contains the operators of the space group. If
  not only the generators are given, a possible set of
  generators will be determined and only those will be saved. The format
  of the string is described in [swsym.str](#swsym-str).
  
`symName`
: Label for the space group.
  
## See Also
  
[swsym.generator](#swsym-generator) \| [swsym.genreduce](#swsym-genreduce)
