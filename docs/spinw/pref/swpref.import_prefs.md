(swpref-import-prefs)=

# swpref.import_prefs method

## Syntax
 
 
`obj = swpref.import_prefs`
 
`obj = swpref.import_prefs(location)`
 
## Description
 
`obj = swpref.import_prefs` loads the preferences given in by the file
`swprefs.json` in the users home folder. It sets the preferences and
returns a new preference object.
 
`obj = swpref.import_prefs(location)` loads the preferences given in by the file
specified by `location`, sets the preferences and returns a new
preference object.
 
## See Also
 
[swpref.export_prefs](#swpref-export-prefs)
