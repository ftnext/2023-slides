# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = '2023_slides'
copyright = '2023, nikkie'
author = 'nikkie'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx_revealjs",
    'sphinx.ext.githubpages',
    "sphinx_design",
]

templates_path = ['_templates']
exclude_patterns = []

language = 'ja'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']

# -- Options for Reveal.js output -------------------------------------------------

revealjs_static_path = ["_static"]
revealjs_script_conf = """
    {
        controls: true,
        progress: true,
        history: true,
        center: true,
        transition: "none",
        slideNumber: "c/t",
    }
"""

revealjs_script_plugins = [
    {
        "name": "RevealHighlight",
        "src": "revealjs4/plugin/highlight/highlight.js",
    },
    {
        "name": "RevealNotes",
        "src": "revealjs4/plugin/notes/notes.js",
    }
]

revealjs_css_files = [
    "revealjs4/plugin/highlight/zenburn.css",
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.1.1/css/all.min.css",
    "css/common.css",
]
