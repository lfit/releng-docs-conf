#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Common conf.py configuration for lf-releng projects."""

import os
import sys

import yaml

import sphinx_bootstrap_theme

with open('../INFO.yaml', 'r') as yaml_file:
    info = yaml.safe_load(yaml_file)

# -- General configuration ------------------------------------------------
needs_sphinx = '1.6'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.viewcode',
    'sphinxcontrib.programoutput',
]

master_doc = 'index'
source_suffix = ['.rst']
templates_path = ['_templates']

# General information about the project.
project = info['project-name']
author = info['author']
copyright = info['copyright']

# The short X.Y version.
version = info['version']
# The full version, including alpha/beta/rc tags.
release = version

language = None
exclude_patterns = []
pygments_style = 'sphinx'
todo_include_todos = True
intersphinx_mapping = {
    'global-jjb': ('http://global-jjb.releng.linuxfoundation.org/en/latest/', None),
    'lfdocs': ('http://docs.releng.linuxfoundation.org/en/latest/', None),
    'lftools': ('http://lftools.releng.linuxfoundation.org/en/latest/', None),
    'python': ('https://docs.python.org/', None),
}

# -- Options for HTML output ----------------------------------------------

html_theme = 'bootstrap'
html_theme_options = {
    'bootswatch_theme': "cerulean",
    'navbar_sidebarrel': False,
    'source_link_position': "footer",
}
html_theme_path = sphinx_bootstrap_theme.get_html_theme_path()
html_logo = info.get('project-logo', '_static/lf-logo-small.png')
html_favicon = 'favicon.ico'
html_static_path = ['_static']
html_sidebars = {
    '**': ['localtoc.html', 'relations.html'],
}

htmlhelp_basename = 'LFRelengDoc'

# If confext.py exists in the same directory as conf.py this is a config
# override file allowing a project to override any configuration in this file.
try:
    print('confext.py found, overriding config.')
    # Insert here so that we can pull in confext.py
    sys.path.insert(0, os.path.abspath('.'))
    # We are purposely allowing * import here to override values in this file
    # noqa
    from confext import *
except ImportError:
    pass
