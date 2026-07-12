(swplot-add)=

# swplot.add

## Syntax
  
`swplot.add(hAdd)`
 
`swplot.add(hAdd,hFigure)`
  
## Description
  
`swplot.add(hAdd)` adds a graphical object to the active swplot figure to
enable continuous rotation with the mouse. The function adds the
graphical objects to as a children to the [hgtransform](https://www.mathworks.com/help/matlab/ref/hgtransform.html).
   
`swplot.add(hAdd,hFigure)` adds the graphical objects to the figure of
the figure handle `hFigure`.
  
## Input Arguments
  
`hAdd`
: Either vector of the handles of the graphical objects, or
  struct with $n_{obj}$ number of elements with a `handle` field each
  containing a graphical object handle. The struct can contain any subset
  of the following fields as well:
  * `name`      Default value is `'general'` if not given. The
                name identifies groups of objects.
  * `text`      Text that is shown in the tooltip when clicking
                on the object.
  * `position`  Position of the object, see [swplot.plot](#swplot-plot) for
                details.
   * `label`    Label that is shown in the legend.
   * `legend`   Type of legend, see [swplot.legend](#swplot-legend) for details.
   * `type`     Type of graphical object, see [swplot.plot](#swplot-plot).
   * `data`     Arbitrary data assigned to the object.
  
`hFigure`
: The handle of the figure or number in the figure title. The
  default value is the active swplot figure if `hFigure` is not given or
  empty matrix.
  
## See Also
  
[swplot] \| [swplot.figure](#swplot-figure) \| [hgtransform](https://www.mathworks.com/help/matlab/ref/hgtransform.html) \| [swplot.delete](#swplot-delete)
