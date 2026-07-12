(spinw)=

# Methods

```{toctree}
:maxdepth: 1
:glob:
:hidden:

methods/*
```

## Syntax
 
`obj = spinw`
 
`obj = spinw(obj)`
 
`obj = spinw(source)`
 
`obj = spinw(figure_handle)`
 
## Description
 
`obj = spinw` constructs an empty spinw class object.
 
`obj = spinw(obj)` constructs a spinw class object from the
parameters defined in `obj`. If `obj` is spinw class, it only checks
the integrity of its internal data structure. If `obj` is struct
type, it creates new spinw object and checks data integrity.
 
`obj = spinw(source)` construct new spinw class object, where
`source` is either a file path pointing to a local `cif` or `fst`
file or a link to an online file.
 
`obj = spinw(figure_handle)` copy the spinw object stored in a
previous structural 3D plot figure, referenced by `figure_handle`.
 
 
The data structure within the spinw object can be accessed by using
[spinw.struct](#spinw-struct) method. All fields of the struct type data behind the
spinw object are accessible through the main field names of the `obj`
object. For example the lattice parameters can be accessed using:
 
```matlab
abc = obj.unit_cell.lat_const
```
 
spinw is a handle class, which means that only the handle of the
object is copied in an assinment command `swobj1 = swobj2`. To create
a copy (clone) of an spinw object use:
 
```matlab
swobj1 = swobj2.copy
```
 
## Properties
 
The data within the `spinw` object is organized into a tree structure
with the main groups and the type of data they store are the
following:
 
* [spinw.lattice](#spinw-lattice) unit cell parameters
* [spinw.unit_cell](#spinw-unit-cell) atoms in the crystallographic unit cell
* [spinw.twin](#spinw-twin) crystal twin parameters
* [spinw.matrix](#spinw-matrix) 3x3 matrices for using them in the Hailtonian
* [spinw.single_ion](#spinw-single-ion) single ion terms of the Hamiltonian
* [spinw.coupling](#spinw-coupling) list of bonds
* [spinw.mag_str](#spinw-mag-str) magnetic structure
* [spinw.unit](#spinw-unit) physical units for the Hamiltonian
* [spinw.cache](#spinw-cache) temporary values
 
## Methods
 
Methods are the different commands that require a `spinw` object as a
first input, thus they can be called as `method1(obj,...)`,
alternatively the equivalent command is `obj.method1(...)`. The list
of public methods is below.
 
### Lattice operations
 
* [spinw.genlattice](#spinw-genlattice) generates crystal lattice
* [spinw.basisvector](#spinw-basisvector) generates lattice vectors
* [spinw.rl](#spinw-rl) generates reciprocal lattice vectors
* [spinw.nosym](#spinw-nosym) reduces symmetry to P0
* [spinw.newcell](#spinw-newcell) transforms lattice
* [spinw.addatom](#spinw-addatom) adds new atom
* [spinw.unitcell](#spinw-unitcell) returns unit cell data
* [spinw.abc](#spinw-abc) returns lattice parameters and angles
* [spinw.atom](#spinw-atom) generates symmetry equivalent atomic positions
* [spinw.matom](#spinw-matom) generates magnetic lattice
* [spinw.natom](#spinw-natom) number of symmetry unrelated atoms
* [spinw.formula](#spinw-formula) returns basic physical properties
* [spinw.disp](#spinw-disp) prints information
* [spinw.symmetry](#spinw-symmetry) returns whether symmetry is defined
    
### Plotting
 
* [spinw.plot](#spinw-plot) plots 3D model
 
### Crystallographic twin operations
 
* [spinw.addtwin](#spinw-addtwin) adds crystallographic twins
* [spinw.twinq](#spinw-twinq) calculates equivalent Q point in twins
* [spinw.notwin](#spinw-notwin) removes all twins
 
### Magnetic structure operations
 
* [spinw.genmagstr](#spinw-genmagstr) generates magnetic structure
* [spinw.magstr](#spinw-magstr) returns single-k magnetic structure representation
* [spinw.magtable](#spinw-magtable) creates tabulated list of all magnetic moments stored in obj
* [spinw.nmagext](#spinw-nmagext) number of magnetic sites
* [spinw.optmagstr](#spinw-optmagstr) general magnetic structure optimizer
* [spinw.optmagk](#spinw-optmagk) determines the magnetic propagation vector
* [spinw.optmagsteep](#spinw-optmagsteep) quench optimization of magnetic structure
* [spinw.anneal](#spinw-anneal) performs simulated annealing of spins
* [spinw.annealloop](#spinw-annealloop) parameter sweep for simulated annealing
* [spinw.structfact](#spinw-structfact) calculates magnetic and nuclear structure factor
    
### Matrix operations
 
* [spinw.addmatrix](#spinw-addmatrix) adds new 3x3 matrix
* [spinw.getmatrix](#spinw-getmatrix) determines the symmetry allowed tensor elements
* [spinw.setmatrix](#spinw-setmatrix) sets exchange tensor values
    
### Spin Hamiltonian generations
 
* [spinw.quickham](#spinw-quickham) quickly generate magnetic Hamiltonian
* [spinw.gencoupling](#spinw-gencoupling) generates bond list
* [spinw.addcoupling](#spinw-addcoupling) assigns an exchange matrix to a bond
* [spinw.addaniso](#spinw-addaniso) assigns anisotropy to magnetic sites
* [spinw.addg](#spinw-addg) assigns g-tensor to magnetic atoms
* [spinw.field](#spinw-field) get/set magnetic field value
* [spinw.temperature](#spinw-temperature) get/set temperature
* [spinw.intmatrix](#spinw-intmatrix) generates interaction matrix
* [spinw.symop](#spinw-symop) generates the bond symmetry operators
* [spinw.setunit](#spinw-setunit) sets the physical units
    
### Solvers
 
* [spinw.spinwave](#spinw-spinwave) calculates spin correlation function using linear spin wave theory
* [spinw.powspec](#spinw-powspec) calculates powder averaged spin wave spectra
* [spinw.energy](#spinw-energy) calculates the ground state energy
* [spinw.moment](#spinw-moment) calculates quantum correction on ordered moment
* [spinw.spinwavesym](#spinw-spinwavesym) calculates symbolic spin wave dispersion
* [spinw.symbolic](#spinw-symbolic) switches between symbolic/numeric mode
* [spinw.fourier](#spinw-fourier) calculates the Fourier transformation of the Hamiltonian
* [spinw.fouriersym](#spinw-fouriersym) calculates the Fourier transformation of the symbolic Hamiltonian
 
### Fitting spin wave spectrum
 
* [spinw.fitspec](#spinw-fitspec) fits experimental spin wave data
* [spinw.matparser](#spinw-matparser) parses parameter vector into matrices
* [spinw.horace](#spinw-horace) spin wave calculator with interface to Horace
    
### Miscellaneous
 
* [spinw.copy](#spinw-copy) clones spinw object
* [spinw.export](#spinw-export) export data into file
* [spinw.table](#spinw-table) outputs easy to read tables of internal data
* [spinw.validate](#spinw-validate) validates spinw object properties
* [spinw.version](#spinw-version) returns the version of SpinW
* [spinw.struct](#spinw-struct) converts properties into struct
* [spinw.clearcache](#spinw-clearcache) clears the cache
* [spinw.spinw](#spinw-spinw) spinw constructor
 
## See also
 
[spinw.copy](#spinw-copy), [spinw.struct](#spinw-struct), [Comparing handle and value classes](https://www.mathworks.com/help/matlab/matlab_oop/comparing-handle-and-value-classes.html)
