Installation
============

pySpinW requires Python 3.10 or newer. Python 3.12 is recommended.

Install
-------

The package is published on PyPI as ``spinw-python``:

.. code-block:: console

   pip install spinw-python

To upgrade an existing install:

.. code-block:: console

   pip install --upgrade spinw-python

Virtual environment
-------------------

We recommend installing into a virtual environment. A minimal setup looks
like this:

.. code-block:: console

   python -m venv .venv
   source .venv/bin/activate

On Windows, activate the environment with ``.venv\Scripts\activate`` instead.

If you prefer Conda or Mamba, create a clean environment first and then run
``pip install spinw-python`` inside it.

Verify
------

After installation, a quick import check is enough:

.. code-block:: console

   python -c "import pyspinw; print(pyspinw.__version__)"
