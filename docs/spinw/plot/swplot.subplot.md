(swplot-subplot)=

# swplot.subplot

## Syntax
  
`swplot.subplot(m,n,p,space)`
  
`swplot.subplot([m,n,p],space)`
 
## Description
  
`swplot.subplot(m,n,p,space)` is equivalent to the [subplot](https://www.mathworks.com/help/matlab/ref/subplot.html)
command, except that the space between axes can be controlled.
  
## Input Arguments
  
`m,n,p`
: Three integer that defines subplot, for details see the
  built-in [subplot](https://www.mathworks.com/help/matlab/ref/subplot.html) command.
  
`space`
: Vector with elements: `[margin hgap vgap]`, where:
  * `margin`  Top and right margin at the figure edge.
  * `hgap`    Left margin and horizontal gap between axes.
  * `vgap`    Bottom margin and vertical gap between axes.
  
## See Also
  
[subplot](https://www.mathworks.com/help/matlab/ref/subplot.html)
