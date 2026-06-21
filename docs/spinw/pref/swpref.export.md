(swpref-export)=

# swpref.export method

## Syntax
 
`success = export(obj,location)`
 
`success = export(obj)`
 
## Description
 
`success = export(obj,location)` writes the preferences given in `obj` to
a file location given by `location`. The file is in a basic `.json`
format.
 
`success = export(obj)` writes the preferences given in `obj` to
the users home folder as `swprefs.json`. The file is in a basic `.json`
format.
 
## See Also
 
[swpref.import](#swpref-import)
