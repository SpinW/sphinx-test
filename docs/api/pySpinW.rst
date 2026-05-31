pySpinW API
===========

The package exports the most common user-facing objects from ``pyspinw`` so
they can be imported directly with ``from pyspinw import *``.

User-facing classes
-------------------

* ``LatticeSite`` - lattice position and spin metadata for a site
* ``UnitCell`` - the crystallographic unit cell
* ``Structure`` - magnetic structure details and site collection
* ``HeisenbergExchange`` - scalar exchange term
* ``DiagonalExchange`` - diagonal exchange matrix
* ``XYExchange`` - exchange with matching x and y components
* ``IsingExchange`` - exchange with only a z term
* ``DMExchange`` - Dzyaloshinskii-Moriya exchange
* ``Anisotropy`` - general anisotropy matrix
* ``AxisMagnitudeAnisotropy`` - anisotropy defined by axis plus signed magnitude
* ``Hamiltonian`` - main object for energy, spectrum, and plotting calculations
* ``SingleCrystal`` - sample model for single-crystal calculations
* ``Multidomain`` - base for multidomain samples
* ``CrystalDomain`` - domain model for single-crystal structures
* ``Twin`` - twinned sample model
* ``Powder`` - powder sample model
* ``PropagationVector`` - general propagation-vector object
* ``CommensuratePropagationVector`` - commensurate propagation-vector helper
* ``TiledSupercell`` - tiled commensurate supercell
* ``SummationSupercell`` - summation-based commensurate supercell
* ``TransformationSupercell`` - transformation-based commensurate supercell
* ``RotationSupercell`` - supercell with rotational mapping
* ``RotationTransform`` - helper for transformation-based supercells

Helper functions
----------------

* ``spacegroup`` - parse a space-group description into a space-group object
* ``generate_sites`` - build site lists from positions and spins
* ``generate_exchanges`` - create exchanges from a site list or structure
* ``generate_structure`` - construct a structure from site and cell data
* ``generate_helical_structure`` - construct a helical magnetic structure
* ``propagation_vectors`` - create propagation-vector helpers
* ``helical_supercell`` - helper for helical structures
* ``rotation_supercell`` - build a rotation supercell
* ``summation_supercell`` - build a summation supercell
* ``axis_anisotropies`` - generate anisotropies from axes and magnitudes
* ``matrix_anisotropies`` - generate anisotropies from matrices
* ``filter`` - build exchange-direction filters
* ``view`` - open the Hamiltonian viewer

Other exported helpers
----------------------

* ``CoordsUnits`` and ``IntensityUnits`` for unit selection
* ``load_cif`` for importing CIF files
* ``set_up_windows_python_parallelisation`` for Windows parallelisation setup
* ``demos``, ``demo_viewer``, and ``demo_chains`` for packaged demos

Internal parameterization objects such as ``HamiltonianParameterization`` are
created by the main classes and are generally not needed directly.

Reference
---------

.. automodule:: pyspinw
   :members:
   :undoc-members:
   :show-inheritance:
