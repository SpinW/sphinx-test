(swfunc-gauss)=

# swfunc.gauss

## Syntax
  
`y = func.gauss(x,p)`
  
## Description
  
`y = func.gauss(x,p)` calculates the $$y$$ values for a Gaussian function
evaluated at $$x$$ and with parameters defined in `p`.
  
## Input Arguments
  
`x`
: Coordinate vector where the function will be evaluated.
  
`p`
: Parameter vector with the following elements `p=[I x0 σ]` where:
  * `I` integrated intensity,
  * `x0` center,
  * `σ` standard deviation.
  
## See Also
  
[swfunc.pvoigt](#swfunc-pvoigt) \| [swfunc.gaussfwhm](#swfunc-gaussfwhm)
