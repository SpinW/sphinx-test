(spinw-nmagext)=

# spinw.nmagext method

## Syntax
 
`nMagExt = nmagext(obj)`
 
## Description
 
`nMagExt = nmagext(obj)` returns the number of magnetic sites
in the magnetic supercell. If the magnetic supercell (stored
in `spinw.mag_str.nExt` is identical to the crystal lattice)
the number of magnetic sites is equal to the number of
magnetic atoms in the unit cell. Where the number of magnetic
atoms in the unit cell can be calculated using [spinw.matom](#spinw-matom).
 
## See Also
 
[spinw.matom](#spinw-matom) \| [spinw.natom](#spinw-natom)
