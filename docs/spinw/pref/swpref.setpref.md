(swpref-setpref)=

# swpref.setpref method

## Syntax
 
`swpref.setpref(name, value)`
 
## Description
 
`swpref.setpref(name, value)` sets the value of `name`
preferences.
 
{% include note.html content=" The preferences are reset after every restart of Matlab, unlike the
Matlab built-in preferences that are persistent between Matlab sessions.
If you want certain preferences to keep after closing matlab, define them
in the `startup.m` file." %}
 
{% include warning.html content=" This is a legacy function. It is better to use 'pref = swpref' and then
use regular 'value = pref.name' or 'get(pref, name)' syntax." %}
 
## See Also
 
[swpref.getpref](#swpref-getpref)
