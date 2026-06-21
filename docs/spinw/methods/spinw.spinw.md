(spinw-spinw)=

# spinw.spinw method

## Syntax
 
`obj = spinw`
 
`obj = spinw(struct)` 
 
`obj = spinw(hFigure)`
 
`obj = spinw(fName)`
 
`obj = spinw(obj)`
 
## Description
 
`obj = spinw` creates an empty SpinW object with default
values.
 
`obj = spinw(struct)` creates a SpinW object from a structure
which has fields that are compatible with the SpinW property
structure.
 
`obj = spinw(hFigure)` clones SpinW object from an swplot
figure or spectral plot figure.
 
`obj = spinw(fName)` imports the file referenced by `fName`.
SpinW is able to import .cif/.fts files for crystal or
magnetic structure from a local file or a web address.
 
`obj = spinw(obj)` checks the input SpinW object for
consistency.
