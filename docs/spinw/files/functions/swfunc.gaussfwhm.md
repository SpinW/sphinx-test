(swfunc-gaussfwhm)=

# swfunc.gaussfwhm

## Syntax
  
`y = func.gaussfwhm(x,p)`
  
## Description
  
`y = func.gaussfwhm(x,p)` calculates the $y$ values for a Gaussian
function evaluated at $x$ and with parameters defined in `p`.
  
## Input Arguments
  
`x`
: Coordinate vector where the function will be evaluated.
  
`p`
: Parameter vector with the following elements `p=[I x0 FWHM]` where:
  * `I`       integrated intensity,
  * `x0`      center,
  * `FWHM`    Full Width at Half Maximum value.
  
## See Also
  
[swfunc.pvoigt](#swfunc-pvoigt) \| [swfunc.gauss](#swfunc-gauss)
