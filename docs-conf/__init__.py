"""
Sphinx Docs Config

To use this file a project should create a conf.cfg file in the same
directory as their conf.py. Conf.py should contain::

    from docs-conf import *

The conf.cfg file should contain at minimum::

    [sphinx]
    project=myproject

And if defaults for 'myproject' exist, they will be loaded from this
package, otherwise a Linux Foundation specific set of defaults will be
set.

Parsing of configs follows this list::

    #.docs-conf/__init__.py
    #.project/conf.cfg (single-value)
    #.docs-conf/defaults/default.cfg or docs-conf/defaults/project.cfg
    #.project/conf.cfg (all values)
    #.project/conf.py

conf.py structure and documentation:
  http://www.sphinx-doc.org/en/stable/config.html
"""
import sphinx_bootstrap_theme
import pkg_resources
import ConfigParser

# Get the project name from the project specific config
project = ConfigParser.ConfigParser({'project': 'default'}).read(['conf.cfg']).get('sphinx', 'project')

# Read in the project's defaults
_project_default_config = "defaults/{}.cfg".format(project)

_config = ConfigParser.SafeConfigParser()
_config.readfp(pkg_resources.resource_stream(__name__, _project_default_config))
_config.read(['conf.cfg'])

# TODO: Presumably settings for each plugin would be saved in their own
# section, and sections would be parsed only if plugins were listed 

# TODO: Each config needs to be imported gracefully (if it doesn't
# exist, set None or something; similar to dict.get

# Parse the config and pull in sphinx conf.py settings
needs_sphinx = _config.get('sphinx', 'needs_sphinx')
extension = _config.get('sphinx', 'extensions').split(',')
templates_path = _config.get('sphinx', 'templates_path').split(',')
source_suffix = _config.get('sphinx', 'source_suffix')
master_doc = _config.get('sphinx', 'master_doc')
project = _config.get('sphinx', 'project')
copyright = _config.get('sphinx', 'copyright')
author = _config.get('sphinx', 'author')
version = _config.get('sphinx', 'version')
release = _config.get('sphinx', 'release')
language = _config.get('sphinx', 'language')
exclude_patterns = _config.get('sphinx', 'exclude_patterns')
pygments_style = _config.get('sphinx', 'pygments_style')
todo_include_todos = _config.get('sphinx', 'todo_include_todos')

html_theme = _config.get('sphinx', 'html_theme')
if html_theme == 'bootstrap':
    import sphinx_bootstrap_theme
    html_theme_path = sphinx_bootstrap_theme.get_html_theme_path()
else:
    html_theme_path = _config.get('sphinx', 'html_theme_path').split(',')
html_logo = _config.get('sphinx', 'html_logo')
html_favicon = _config.get('sphinx', 'html_favicon')
html_static_path = _config.get('sphinx', 'html_static_path').split(',')
htmlhelp_basename = _config.get('sphinx', 'htmlhelp_basename')

html_theme_options = {
    'bootswatch_theme': "journal",
    'navbar_sidebarrel': False,
}

latex_elements = {}

latex_documents = [
    (master_doc, '{}.tex'.format(project), '{} Documentation'.format(project),
     '{} Project'.format(project), 'manual'),
]

man_pages = [
    (master_doc, project, '{} Documentation'.format(project),
     [author], 1)
]

texinfo_documents = [
    (master_doc, project, '{} Documentation'.format(project),
     author, project, 'One line description of project.',
     'Miscellaneous')]

html_sidebars = {'**': ['localtoc.html', 'relations.html'],}
