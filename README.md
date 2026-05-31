# SpinW Sphinx Docs

This repository builds a Sphinx documentation site for SpinW, pySpinW, and
SpinWcore.

## Sphinx setup

- Source directory: `docs/`
- Entry page: `docs/index.rst`
- Config file: `docs/conf.py`
- Theme: `alabaster`(default)
- Extensions:
  - `sphinx.ext.autodoc` for the generated pySpinW API page
  - `sphinx.ext.mathjax` for equations
- Custom CSS: `docs/_static/site.css`

## Customizations

On top of the Alabaster default theme, the site customizes:

- sidebar logo sizing and hidden logo text
- more visible sidebar section captions
- brighter Flask-like code blocks
