(swfiles)=

# Functions in swfiles

This folder contains all the spectral functions and general functions
that are related to SpinW.
 
## Files
 
### Transforming and plotting calculated spin wave spectrum
 
These functions operate on the calculated spectra, which is the output of
[spinw.spinwave](#spinw-spinwave) or [spinw.powspec](#spinw-powspec) commands. They enable to post process
the calculated spin-spin correlation function, including instrumental
resolution, cross section calculation, binning etc.
 
* [sw_econtract](#sw-econtract) converts (Q,E) values to Q values for diffraction instrument
* [sw_egrid](#sw-egrid) calculates energy bins of a spectrum 
* [sw_filelist](#sw-filelist) lists spinw objects in the Matlab workspace or in a .mat file
* [sw_instrument](#sw-instrument) convolutes spectrum with resolution function
* [sw_magdomain](#sw-magdomain) calculates the spin-spin correlation function for magnetic domains
* [sw_neutron](#sw-neutron) calculates neutron scattering cross section
* [sw_omegasum](#sw-omegasum) removes degenerate and ghost magnon modes from spectrum
* [sw_plotspec](#sw-plotspec) plots spectrum
* [sw_xray](#sw-xray) calculates x-ray scattering cross section
 
### Generate list of vectors in reciprocal space
 
These two functions can generate a set of 3D points in reciprocal space
defining either a path made out of straigh lines or a volume.
 
* [sw_qgrid](#sw-qgrid) creates a Q grid
* [sw_qscan](#sw-qscan) creates continuous line between coordinates
 
### Resolution claculation and convolution
 
These functions can import Energy resolution function and convolute it
with arbitrary multidimensional dataset
 
* [sw_res](#sw-res) fits energy resolution with polynomial
* [sw_resconv](#sw-resconv) convolution of a matrix and a Gaussian
* [sw_tofres](#sw-tofres) convolutes the spectrum with a Q bin
 
### SpinW model related functions
 
* [sw_extendlattice](#sw-extendlattice) creates superlattice
* [sw_fstat](#sw-fstat) calculates thermodynamical averages
* [sw_model](#sw-model) creates predefined spin models
* [sw_bonddim](#sw-bonddim) find dimensionality of a periodic bond network
 
### Constraint functions
 
Contraint functions for [spinw.optmagstr](#spinw-optmagstr).
 
* [gm_planar](#gm-planar) planar magnetic structure constraint function 
* [gm_planard](#gm-planard) planar magnetic structure constraint function 
* [gm_spherical3d](#gm-spherical3d) magnetic structure constraint function with spherical parameterisation
* [gm_spherical3dd](#gm-spherical3dd) magnetic structure constraint function with spherical parameterisation
 
### Geometrical calculations
 
Basic geometrical calculators, functions to generatate rotation
operators, generate Cartesian coordinate system from a set of vectors,
calculate normal vector to a set of vector, etc.
 
* [sw_basismat](#sw-basismat) determines allowed tensor components in a given point group symmetry
* [sw_cartesian](#sw-cartesian) creates a right handed Cartesian coordinate system
* [sw_fsub](#sw-fsub) simple graph vertex coloring
* [sw_mattype](#sw-mattype) classifies square matrices
* [sw_nvect](#sw-nvect) determines the best normal vector for the set of vectors
  sw_quadell  
* [sw_mirror](#sw-mirror) mirrors a 3D vector
* [sw_rot](#sw-rot) rotates vectors in 3D
* [sw_rotmat](#sw-rotmat) generates 3D rotation matrix
* [sw_rotmatd](#sw-rotmatd) generates 3D rotation matrix
 
### Text and graphical input/output for different high level commands
 
* [sw_multicolor](#sw-multicolor) overlays monochrome maps into a single RGB map
* [sw_parstr](#sw-parstr) parses input string
* [sw_timeit](#sw-timeit) timer and remaining time estimator
 
### Acessing the SpinW database
 
Functions to read the different data files that store information on
atomic properties, such as magnetic form factor, charge, etc.
  
* [sw_atomdata](#sw-atomdata) returns information on chemical elements
* [sw_cff](#sw-cff) returns the atomic charge form factor values for X-ray scattering
* [sw_mff](#sw-mff) returns the magnetic form factor values and coefficients
* [sw_nb](#sw-nb) returns the bound coherent neutron scattering length
 
### Useful physics functions
 
The two functions can calculate the Bose factor and convert
energy/momentum units, both usefull for neutron and x-ray scattering.
 
* [sw_bose](#sw-bose) coefficient for boson correlation functions
* [sw_converter](#sw-converter) converts energy and momentum units for a given particle
 
### Import functions
 
Functions to import tables in text format.
 
* [sw_import](#sw-import) create SpinW object from .cif and FullProf Studio .fst files
* [sw_readspec](#sw-readspec) read spin wave dispersion data from file
* [sw_readtable](#sw-readtable) reads tabular data from text
 
### Miscellaneous
 
* [swdoc](#swdoc) opens the SpinW documentation
* [sw_freemem](#sw-freemem) calculates the available memory
* [sw_readparam](#sw-readparam) parse input arguments
* [sw_rootdir](#sw-rootdir) path to the SpinW folder
* [sw_uniquetol](#sw-uniquetol) returns the unique column vectors within tolerance
* [sw_update](#sw-update) updates the SpinW installation from the internet
* [sw_version](#sw-version) returns the installed version of SpinW
* [sw_mex](#sw-mex) compiles and tests the mex files
