(sw-omegasum)=

# sw_omegasum

## Syntax
  
`spec = sw_omegasum(spec,Name,Value)`
  
## Description
  
`spec = sw_omegasum(spec,Name,Value)` removes the degenerate modes from
the dispersion stored in `spec.omega` and sorts the modes according to
increasing energy. It also removes ghost modes if a lower intensity limit
is given.
   
The degenerate energies are substituted with `NaN` values.
 
{% include warning.html content=" Be carefull, after this function [sw_egrid](#sw-egrid) won't work properly.
This function won't work with spectra of multiple twins." %}
  
## Name-Value Pair Arguments
  
`'tol'`
: Energy tolerance, within the given value two energies are considered
  equal. Default value is $$10^{-5}$$.
  
`'zeroint'`
: The minimum intensity value, below which the mode is removed. Default
  value is 0 (no modes are dropped due to weak intensity).
  
`'emptyval'`
: Value that is assigned to modes that are removed. Default value is NaN
  (good for plotting). 0 can be used if further numerical analysis, such
  as binning will be applied.
  
## See Also
  
[spinw.spinwave](#spinw-spinwave) \| [sw_egrid](#sw-egrid)
