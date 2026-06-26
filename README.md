# SpinW Sphinx Docs

This repository builds a Sphinx documentation site for SpinW, pySpinW, and
SpinWcore.

## Sphinx setup

- Source directory: `docs/`
- Entry page: `docs/index.rst`
- Config file: `docs/conf.py`
- Theme: `pydata_sphinx_theme`
- Extensions:
  - `sphinx.ext.autodoc` for the generated pySpinW API page
  - `sphinx.ext.autosummary`
  - `sphinx.ext.napoleon`
  - `sphinx.ext.mathjax` for equations
  - `myst_parser` (with `dollarmath` and `deflist`) for Markdown sources
- Custom CSS: `docs/_static/site.css`

## Customizations

On top of the pydata-sphinx-theme defaults, `site.css` styles homepage-specific
elements:

- `project-cards` / `project-card` grid for the project tiles, with hover states
- `project-logo` and `project-badges` layout inside each card
- `partner-table` / `partner-logo` sizing for the partner logo grid
- navbar spacing tweaks (`.bd-navbar-elements.navbar-nav`)
