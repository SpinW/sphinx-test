pySpinW API
===========

Reference for the ``pyspinw`` Python package. Modules are grouped by role;
follow any link for the detailed function and class reference.

.. currentmodule:: pyspinw

Sample and structure
--------------------

.. autosummary::
   :toctree: generated
   :nosignatures:

   sample
   basis
   site
   sitemeta
   cell_offsets
   lattice_analysis
   lattice_distances
   structures
   subsystems

Exchange and Hamiltonian
------------------------

.. autosummary::
   :toctree: generated
   :nosignatures:

   exchange
   exchangegroup
   exchangemetadata
   batch_exchanges
   hamiltonian
   anisotropy

Calculations and spectroscopy
-----------------------------

.. autosummary::
   :toctree: generated
   :nosignatures:

   calculations
   polarisation
   path

.. note::

   ``pyspinw.experiment``, ``pyspinw.instrument`` and ``pyspinw.measurement``
   currently fail to import in the upstream package (broken relative imports);
   they will be listed here once that is fixed.

Symmetry and I/O
----------------

.. autosummary::
   :toctree: generated
   :nosignatures:

   symmetry
   cif
   serialisation

Utilities
---------

.. autosummary::
   :toctree: generated
   :nosignatures:

   checks
   constants
   data
   interface
   tolerances
   units
   util
