(swplot-activefigure)=

# swplot.activefigure

## Syntax
  
`hFigure = swplot.activefigure`
 
`swplot.activefigure(hFigure)`
  
## Description
  
`hfigure = swplot.activefigure` returns the handle of the active swplot
figure and makes it selected. If no swplot figure exists, the function
throws an error.
   
`swplot.activefigure(hFigure)` makes the figure of `hFigure` handle the
active figure.
  
## Input Arguments
  
`hFigure`
: Figure handle or figure number.
  
## Output Arguments
  
`hFigure`
: Handle of the active swplot figure.
  
## See Also
  
[swplot.figure](#swplot-figure)
