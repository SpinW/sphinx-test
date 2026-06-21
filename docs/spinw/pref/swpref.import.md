(swpref-import)=

# swpref.import method

## Syntax
 
  
`obj = import(obj)`
 
`obj = import(obj,location)`
 
## Description
 
`obj = import(obj)` loads the preferences given in by the file
`swprefs.json` in the users home folder. It sets the preferences and
returns a new preference object.
 
`obj = import(obj,location)` loads the preferences given in by the file 
specified by `location`, sets the preferences and returns a new
preference object.
 
## See Also
 
[swpref.export](#swpref-export)
