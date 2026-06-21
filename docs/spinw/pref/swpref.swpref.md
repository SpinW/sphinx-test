(swpref-swpref)=

# swpref.swpref method

## Syntax
 
`pref = swpref`
 
`pref = swpref('default')`
 
 
## Description
 
`pref = swpref` retrieves and creates a preference object.
 
`pref = swpref('default')` resets all preferences to default values.
 
 
{% include note.html content=" The preferences are reset after every restart of Matlab, unlike the
Matlab built-in preferences that are persistent between Matlab sessions.
If you want certain preferences to keep after closing matlab, use the
'pref.export(fileLocation)' and 'pref.import(fileLocation)' functions.
These can be added to your startup file." %}
 
## See Also
 
[swpref.get](#swpref-get), [swpref.set](#swpref-set)
