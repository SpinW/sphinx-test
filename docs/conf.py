# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "pySpinW"
copyright = "2026, pySpinW Devs"
author = "pySpinW Devs"
release = "0.0.01"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.mathjax",
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "alabaster"

html_static_path = ["_static"]
html_css_files = [
    "site.css",
]

html_theme_options = {
    "logo": "img/pyspinw_logo.png",
    "logo_name": False,
    "page_width": "1040px",
    "sidebar_collapse": True,
    "sidebar_width": "240px",
}
