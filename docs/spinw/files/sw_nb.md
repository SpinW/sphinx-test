(sw-nb)=

# sw_nb

## Syntax
  
`bc = sw_nb(atomname)`
  
## Description
  
`bc = sw_nb(atomname)` returns the bound coherent neutron scattering
length of a given nucleus in fm units. The function reads the stored data
from the [isotope.dat](matlab:edit([sw_rootdir,'dat_files',filesep,'isotope.dat'])) file.
  
## Input Arguments
  
`atomName`
: String, contains the name of the atom or isotope (e.g. `'13C'` stands
  for the carbon-13 isotope).
  
## Output Arguments
  
`bc`
: Value of the bound coherent neutron scattering length in units of fm.
