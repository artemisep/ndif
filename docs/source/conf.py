# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os, sys
from datetime import datetime
#temp comment out
#sys.path.insert(0, os.path.abspath('../../'))  # so autodoc can import ndif/*

#added
# Make the code importable for autodoc
ROOT = os.path.abspath(os.path.join(__file__, "..", "..", ".."))
SRC  = os.path.join(ROOT, "src")
if os.path.isdir(os.path.join(SRC, "ndif")):
    sys.path.insert(0, SRC)      # src/ layout (NDIF uses this)
elif os.path.isdir(os.path.join(ROOT, "ndif")):
    sys.path.insert(0, ROOT)     # flat layout fallback
else:
    print("[conf] WARNING: could not find ndif under src/ or repo root")

#added end

project = 'NDIF'
author = 'NDIF Team'
copyright = f'{datetime.now():%Y}, NDIF'
extensions = [
    'myst_parser',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'sphinx.ext.intersphinx',
    'sphinx_autodoc_typehints',
    'sphinx_copybutton',
    'sphinx_design',
    'sphinxcontrib.openapi',
    'sphinx_tabs.tabs',
]
autosummary_generate = True
autodoc_typehints = 'description'
napoleon_google_docstring = True
napoleon_numpy_docstring = True

html_theme = 'pydata_sphinx_theme'
html_title = 'NDIF Documentation'
html_static_path = ['_static']
#set to this later when the logo is available
#html_logo = '_static/ndif_logo.png'  # add later if you want
html_logo = None
#end set logo

html_theme_options = {
    "show_prev_next": False,
    "external_links": [
        {"name": "GitHub", "url": "https://github.com/ndif-team/ndif"},
        {"name": "NNsight Docs", "url": "https://nnsight.net/documentation/"},
    ],
    "navigation_depth": 3,
}

# Markdown config
myst_enable_extensions = ["colon_fence", "deflist", "fieldlist", "attrs_block"]

# Intersphinx (link to external APIs like Python, PyTorch, FastAPI)
intersphinx_mapping = {
    "python": ("https://docs.python.org/3", {}),
    "torch": ("https://pytorch.org/docs/stable", {}),
    "fastapi": ("https://fastapi.tiangolo.com/", {}),
}

# If your package root is `src/ndif`, use:
# sys.path.insert(0, os.path.abspath('../../src'))

#added
root_doc = 'index'
