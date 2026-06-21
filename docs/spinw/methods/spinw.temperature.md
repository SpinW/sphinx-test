(spinw-temperature)=

# spinw.temperature method

## Syntax
  
`temperature(obj, T)`
 
`T = temperature(obj)`
  
## Description
  
`temperature(obj, T)` sets the temperature stored in `obj` to `T`, where
`T` is scalar. The units of temerature is determined by the
`spinw.unit.kB` value, default unit is Kelvin.
   
`T = temperature(obj)` returns the current temperature value stored in
`obj`.
