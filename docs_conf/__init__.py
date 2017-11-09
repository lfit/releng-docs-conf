"""
Sphinx Docs Config

Configure sphinx-doc through an ini file.
"""

import os.path
import pkg_resources
import ConfigParser

from importlib import import_module


def collect_project_and_config():
    """
    Extract the project from the calling config, and use that to lookup
    project defaults.

    Return the project name and merged configs from the calling project
    and per-project defaults.
    """
    if not os.path.isfile('conf.cfg'):
	raise IOError("No conf.cfg file found at: {}".format(os.getcwd()))

    # Get the project name from the project specific config
    _project_config = ConfigParser.ConfigParser()
    _project_config.readfp(pkg_resources.resource_stream(__name__, 'defaults/default.cfg'))
    _project_config.read(['conf.cfg'])

    _project = _project_config.get('sphinx', 'project')

    # Create a new config from the project defaults, and those listed in
    # conf.cfg
    _config = ConfigParser.ConfigParser()
    # Read in the project's defaults
    _project_default_config = "defaults/{}.cfg".format(_project)
    if os.path.isfile(_project_default_config):
        _config.readfp(pkg_resources.resource_stream(__name__, _project_default_config))
    else:
        _config.readfp(pkg_resources.resource_stream(__name__, 'defaults/default.cfg'))
    _config.read(['conf.cfg'])

    return _project, _config

project, _config = collect_project_and_config()

# Parse the bare defaults
#  - author
#  - copyright
#  - exclude_patterns
#  - extensions
#  - html_favicon
#  - html_logo
#  - html_sidebars
#  - html_static_path
#  - html_theme
#  - html_theme_options
#  - html_theme_path
#  - htmlhelp_basename
#  - intersphinx_mapping
#  - language
#  - latex_documents
#  - latex_elements
#  - man_pages
#  - master_doc
#  - needs_sphinx
#  - project
#  - pygments_style
#  - release
#  - source_suffix
#  - templates_path
#  - texinfo_documents
#  - todo_include_todos
#  - version

# Parse the config and pull in sphinx conf.py settings
author = _config.get('sphinx', 'author')
copyright = _config.get('sphinx', 'copyright')
exclude_patterns = _config.get('sphinx', 'exclude_patterns')
extension = _config.get('sphinx', 'extensions').split(',')
html_favicon = _config.get('sphinx', 'html_favicon')
html_logo = _config.get('sphinx', 'html_logo')
html_sidebars = {'**': ['localtoc.html', 'relations.html'],}
html_static_path = _config.get('sphinx', 'html_static_path').split(',')
html_theme = _config.get('sphinx', 'html_theme')
html_theme_options = {
    'bootswatch_theme': "journal",
    'navbar_sidebarrel': False,
}
html_theme_path = _config.get('sphinx', 'html_theme_path')
# # TODO: Document these new value
# # if html_theme_module is set, also require html_theme_path
# html_theme_module = _config.get('sphinx', 'html_theme_module')
#
# html_theme_path = sphinx_bootstrap_theme.get_html_theme_path()
# else:
#     html_theme_path = _config.get('sphinx', 'html_theme_path').split(',')
htmlhelp_basename = _config.get('sphinx', 'htmlhelp_basename')
intersphinx_mapping = None
language = _config.get('sphinx', 'language')
master_doc = _config.get('sphinx', 'master_doc')
latex_documents = [
    (master_doc, '{}.tex'.format(project), '{} Documentation'.format(project),
     '{} Project'.format(project), 'manual'),
]
latex_elements = {}
man_pages = [
    (master_doc, project, '{} Documentation'.format(project),
     [author], 1)
]
needs_sphinx = _config.get('sphinx', 'needs_sphinx')
project = _config.get('sphinx', 'project')
pygments_style = _config.get('sphinx', 'pygments_style')
release = _config.get('sphinx', 'release')
source_suffix = _config.get('sphinx', 'source_suffix')
templates_path = _config.get('sphinx', 'templates_path').split(',')
texinfo_documents = [
    (master_doc, project, '{} Documentation'.format(project),
     author, project, 'One line description of project.',
     'Miscellaneous')]
todo_include_todos = _config.get('sphinx', 'todo_include_todos')
version = _config.get('sphinx', 'version')
