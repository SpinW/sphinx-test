(swplot-delete)=

# swplot.delete

## Syntax
  
`swplot.delete(objID)`
 
`swplot.delete(hFigure,objID)`
  
## Description
  
`swplot.delete(objID)` deletes objects and their data that corresponds to
the given unique `objID` (integer number) on the active swplot figure.
 
`swplot.delete(hFigure,objID)` deletes objects from the swplot figure
corresponding to `hFigure` handle.
   
If `objID` equals to 0, all objects will be deleted from the swplot
figure.
   
## See Also
 
[swplot.figure](#swplot-figure) \| [swplot.add](#swplot-add)
