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

html_theme = "sphinx_book_theme"

html_static_path = ["_static"]
html_logo = "_static/img/pyspinw_logo.png"
html_css_files = [
    "site.css",
]

html_theme_options = {
    "home_page_in_toc": False,
    "show_navbar_depth": 1,
    "max_navbar_depth": 4,
    "collapse_navbar": True,
}
