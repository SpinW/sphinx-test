(swplot-view)=

# swplot.view

## Syntax
  
`swplot.view(ax)`
  
`swplot.view(ax, hFigure)`
 
## Description
  
`swplot.view(ax)` controls the plane that the camera sees. The
preconfigured options are pairs of $abc$ axes or $hkl$ reciprocal lattice
axes.
  
## Input Arguments
  
`ax`
: String that controls the view plane, recognised values are:
  * `'ab'`\|`'bc'`\|`'ac'`  the two axes define the view plane,
  * `'hk'`\|`'kl'`\|`'hl'`  the two reciprocal lattice vectors define
                            the view plane.
  
`hFigure`
: Handle of the swplot figure window, default value is the active swplot
  figure.
