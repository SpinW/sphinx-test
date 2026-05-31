SpinW
=====

.. raw:: html

   <section class="landing-hero">
     <div class="landing-hero__content">
       <p class="landing-kicker">SpinW Documentation</p>
       <h1>SpinW and pySpinW</h1>
       <p class="landing-lead">
         Libraries for plotting and numerically simulating magnetic structures
         and excitations from spin Hamiltonians.
       </p>
       <div class="landing-actions">
         <a class="landing-button landing-button--primary" href="pyspinw/installation.html">Install pySpinW</a>
         <a class="landing-button" href="spinw/installation.html">Install SpinW</a>
         <a class="landing-button" href="https://github.com/SpinW/spinw/issues">Report Issue</a>
       </div>
     </div>
   </section>

.. raw:: html

   <section class="landing-section landing-section--projects">
     <div class="landing-section__heading">
       <p class="landing-kicker">The Projects</p>
       <h2>One documentation home for the SpinW ecosystem</h2>
     </div>
     <div class="project-grid">
       <a class="project-card" href="spinw/overview.html">
         <span class="project-card__label">MATLAB</span>
         <strong>SpinW</strong>
         <span>Original SpinW implementation for MATLAB.</span>
       </a>
       <a class="project-card" href="pyspinw/overview.html">
         <span class="project-card__label">Python</span>
         <strong>pySpinW</strong>
         <span>Python implementation of SpinW.</span>
       </a>
       <a class="project-card" href="spinwcore.html">
         <span class="project-card__label">C++</span>
         <strong>SpinWcore</strong>
         <span>Core routines intended for speed-critical calculations.</span>
       </a>
     </div>
   </section>

Features
--------

SpinW solves spin Hamiltonians using classical and quasi-classical numerical
methods:

.. math::

   H = \sum_{i,j} S_i J_{ij} S_j
       + \sum_i S_i A_i S_i
       + \mu_B \sum_i B g_i S_i

where :math:`S_i` are spin vector operators, :math:`J_{ij}` are exchange
matrices, :math:`A_i` are anisotropy matrices, :math:`B` is the external
magnetic field, and :math:`g_i` is the g-tensor.

.. raw:: html

   <div class="feature-grid">
     <section>
       <h3>Crystal Structures</h3>
       <ul>
         <li>Define arbitrary unit cells with space groups or symmetry operators.</li>
         <li>Define magnetic and non-magnetic atoms with arbitrary moment sizes.</li>
         <li>Create publication-quality crystal structure plots.</li>
       </ul>
     </section>
     <section>
       <h3>Magnetic Structures</h3>
       <ul>
         <li>Define 1D, 2D, and 3D magnetic structures.</li>
         <li>Represent incommensurate structures with rotating coordinates.</li>
         <li>Generate and plot structures on magnetic supercells.</li>
       </ul>
     </section>
     <section>
       <h3>Magnetic Interactions</h3>
       <ul>
         <li>Assign interactions to neighboring atoms by distance.</li>
         <li>Use Heisenberg, Dzyaloshinskii-Moriya, anisotropic, and tensor exchange.</li>
         <li>Calculate symmetry-allowed tensor elements from space groups.</li>
       </ul>
     </section>
     <section>
       <h3>Simulations</h3>
       <ul>
         <li>Run energy minimization, simulated annealing, and thermodynamic calculations.</li>
         <li>Simulate neutron diffraction, diffuse scattering, and spin-wave spectra.</li>
         <li>Calculate powder-averaged spectra and neutron scattering cross sections.</li>
       </ul>
     </section>
   </div>

Documentation
-------------

.. toctree::
   :maxdepth: 2
   :caption: SpinW Docs

   spinw/installation
   spinw/tutorials
   spinw/overview

.. toctree::
   :maxdepth: 2
   :caption: pySpinW Docs

   pyspinw/installation
   pyspinw/examples
   pyspinw/overview
   api/pySpinW

.. toctree::
   :maxdepth: 2
   :caption: Resources

   resources/faq
   resources/publications
   resources/presentations
   resources/contact
   spinwcore
