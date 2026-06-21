(spinw-annealloop)=

# spinw.annealloop method

## Syntax
  
`stat = anneal(obj,Name,Value)`
  
## Description
  
`stat = annealloop(obj,Name,Value)` performs simulated annealing while
stepwise changing a selected parameter such as temperature or magnetic
field while measuring thermodynamic properties. The function has the same
parameters as [spinw.anneal](#spinw-anneal) plus an additional
   
  
## Input Arguments
  
`obj`
: [spinw](#spinw) object.
  
## Name-Value Pair Arguments
  
`'func'`
: Function that changes the parameters in the spinw object in every
  loop. Default function is to change the temperature:
  ```matlab
  @temperature(obj,x)
  ```
  The function takes two inputs a [spinw](#spinw) object and a parameter value
  (ir values in a vector) and changes the correspondign property inside
  the object.
  
`'x'`
: Matrix of values of the loop parameter, with dimensions of
  $$[n_{par}\times n_{loop}]$$. Default value is 1. In the i-th loop the
  loop function is called as:
  ```matlab
  func(obj,x(:,i));
  ```
  
`'saveObj'`
: If `true`, the spinw object is saved after every annealing step for
  debugging purposes. Default is `false`.
 
`'tid'`
: Determines if the elapsed and required time for the calculation is
  displayed. The default value is determined by the `tid` preference
  stored in [swpref](#swpref). The following values are allowed (for more details
  seee [sw_timeit](#sw-timeit)):
  * `0` No timing is executed.
  * `1` Display the timing in the Command Window.
  * `2` Show the timing in a separat pup-up window.
  
## Output Arguments
  
Same output as of [spinw.anneal](#spinw-anneal), just the struct is packaged into a cell
with $$n_{loop}$$ number of elements.
 
## Reference
 
   Kirkpatrick, S., Gelatt, C.D., & Vecchi, M.P. (1983). Optimization by
   Simulated Annealing. _Science, 220_, 671-680.
  
## See Also
  
[spinw](#spinw) \| [spinw.anneal](#spinw-anneal) \| [sw_fsub](#sw-fsub) \| [sw_fstat](#sw-fstat)
