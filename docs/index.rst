.. rst-class:: home-title

SpinW
=====

.. rst-class:: home-intro

*SpinW* and *pySpinW* are libraries that can plot and numerically simulate
magnetic structures and excitations of a given spin Hamiltonian using
classical Monte Carlo simulation and linear spin-wave theory. SpinW and
pySpinW are written for MATLAB and Python respectively.

.. rst-class:: home-links

Quick links:
`Install SpinW <spinw/installation.html>`_ |
`Install pySpinW <pyspinw/installation.html>`_ |
`Report Issue <https://github.com/SpinW/spinw/issues>`_

The Projects
------------

.. container:: project-cards

   .. container:: project-card

      .. image:: _static/img/spinw3_logo.png
         :alt: SpinW logo
         :class: project-logo

      `SpinW <spinw/overview.html>`_

      Original SpinW written in MATLAB.

      .. container:: project-badges

         .. image:: https://img.shields.io/github/forks/spinw/SpinW.svg?style=social&label=Fork
            :alt: SpinW forks
            :target: https://github.com/spinw/SpinW/network/members

         .. image:: https://img.shields.io/github/stars/spinw/SpinW.svg?style=social&label=Stars
            :alt: SpinW stars
            :target: https://github.com/spinw/SpinW/stargazers

   .. container:: project-card

      .. image:: _static/img/pyspinw_logo.png
         :alt: pySpinW logo
         :class: project-logo

      `pySpinW <pyspinw/overview.html>`_

      Python implementation of SpinW.

      .. container:: project-badges

         .. image:: https://img.shields.io/github/forks/spinw/pySpinW.svg?style=social&label=Fork
            :alt: pySpinW forks
            :target: https://github.com/spinw/pySpinW/network/members

         .. image:: https://img.shields.io/github/stars/spinw/pySpinW.svg?style=social&label=Stars
            :alt: pySpinW stars
            :target: https://github.com/spinw/pySpinW/stargazers

   .. container:: project-card

      .. image:: _static/img/spinwcore_logo.svg
         :alt: SpinWcore logo
         :class: project-logo

      `SpinWcore <spinwcore.html>`_

      SpinW core functions written in C++ for speed.

      .. container:: project-badges

         .. image:: https://img.shields.io/github/forks/spinw/SpinWcore.svg?style=social&label=Fork
            :alt: SpinWcore forks
            :target: https://github.com/spinw/SpinWcore/network/members

         .. image:: https://img.shields.io/github/stars/spinw/SpinWcore.svg?style=social&label=Stars
            :alt: SpinWcore stars
            :target: https://github.com/spinw/SpinWcore/stargazers

Features
--------

SpinW can solve the following spin Hamiltonian using classical and
quasi-classical numerical methods:

.. math::

   H = \sum_{i,j} S_i J_{ij} S_j
       + \sum_i S_i A_i S_i
       + B \sum_i g_i S_i

where :math:`S_i` are spin vector operators, :math:`J_{ij}` are 3x3 matrices
describing pair coupling between spins, :math:`A_{ij}` are 3x3 anisotropy
matrices, :math:`B` is the external magnetic field, and :math:`g_i` is the
g-tensor.

Crystal structures
~~~~~~~~~~~~~~~~~~

* Definition of crystal lattice with arbitrary unit cell, using space group or
  symmetry operators.
* Definition of non-magnetic atoms and magnetic atoms with arbitrary moment
  size.
* Publication-quality plotting of crystal structures, including atoms, labels,
  axes, polyhedra, anisotropy ellipsoids, and DM vectors.

Magnetic structures
~~~~~~~~~~~~~~~~~~~

* Definition of 1D, 2D, and 3D magnetic structures.
* Representation of incommensurate structures using a rotating coordinate
  system or complex basis vectors.
* Generation and plotting of magnetic structures on magnetic supercells.

Magnetic interactions
~~~~~~~~~~~~~~~~~~~~~

* Assignment of magnetic interactions to neighbouring magnetic atoms based on
  distance.
* Heisenberg, Dzyaloshinskii-Moriya, anisotropic, and general 3x3 exchange
  tensors.
* Single-ion anisotropy tensor and Zeeman energy in homogeneous magnetic field.
* Symmetry-allowed tensor elements calculated from the crystallographic space
  group.

Simulation of magnetic structures
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Classical energy minimization and simulated annealing.
* Thermodynamic properties, magnetic structure factors, neutron diffraction,
  and diffuse scattering.
* Magnetic excitations in commensurate and incommensurate structures using
  linear spin-wave theory.
* Spin-wave dispersion, spin-spin correlation functions, neutron scattering
  cross sections, and powder-averaged spectra.

Plotting and fitting spin-wave spectra
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Plotting of dispersions, correlation functions, and convoluted spectra.
* Integration into Horace for comparison with time-of-flight neutron data.
* Fitting Hamiltonian parameters robustly against measured spectra.

Our Partners
------------

.. list-table::
   :widths: 1 1 1
   :header-rows: 0
   :class: partner-table

   * - .. image:: _static/img/ess_logo.png
          :alt: European Spallation Source
          :class: partner-logo
     - .. image:: _static/img/isis_logo.png
          :alt: ISIS, Science & Technology Facilities Council
          :class: partner-logo
     - .. image:: _static/img/psi_logo.png
          :alt: Paul Scherrer Institut
          :class: partner-logo
   * - .. image:: _static/img/hzb_logo.gif
          :alt: Helmholtz-Zentrum Berlin
          :class: partner-logo
     - .. image:: _static/img/nbia_logo.png
          :alt: Niels Bohr International Academy
          :class: partner-logo
     -

.. toctree::
   :maxdepth: 2
   :hidden:

   news

.. toctree::
   :maxdepth: 2
   :hidden:
   :caption: SpinW Docs

   spinw/installation
   spinw/tutorials
   SpinW Issues <https://github.com/SpinW/spinw/issues>
   spinw/class
   spinw/properties
   spinw/methods
   spinw/files
   spinw/plot
   spinw/pref
   spinw/sym
   spinw/overview

.. toctree::
   :maxdepth: 2
   :hidden:
   :caption: pySpinW Docs

   pyspinw/installation
   pyspinw/examples
   pyspinw/overview
   api/pySpinW

.. toctree::
   :maxdepth: 2
   :hidden:
   :caption: Resources

   resources/faq
   resources/publications
   resources/presentations

.. toctree::
   :maxdepth: 2
   :hidden:
   :caption: Report Issue

   SpinW <https://github.com/SpinW/spinw/issues>
   pySpinW <https://github.com/SpinW/pySpinW/issues>

   resources/contact
