"""
Sphinx Docs Config

Configure sphinx-doc through an ini file.
"""

import os.path
import pkg_resources

import sphinx_bootstrap_theme
import yaml


def _merge_yaml(data, merge):
    """Merges dictionary 'merge' into 'data'"""
    if isinstance(data, dict) and isinstance(merge, dict):
        for k,v in merge.iteritems():
            if k not in data:
                data[k] = v
            else:
                data[k] = merge(data[k], v)
    return data


def collect_project_and_config():
    """Pull project and configuration by merging all config sources

    Order of precedence:

    1) local conf.yaml
    2) defaults/PROJECT.yaml
    3) defaults/default.yaml

    Return the project name and merged configs from the calling project
    and per-project defaults.
    """
    if not os.path.isfile('conf.yaml'):
        raise IOError("No conf.yaml file found at: {}".format(os.getcwd()))

    with open('conf.yaml', 'r') as f:
        _config = yaml.load(f)

    _project = _config.get('project', None)
    print(_project)

    # # Get the project name from the project specific config
    # _project_config = ConfigParser.ConfigParser()
    # _project_config.readfp(pkg_resources.resource_stream(__name__, 'defaults/default.cfg'))
    # _project_config.read(['conf.cfg'])
    #
    # _project = _project_config.get('sphinx', 'project')
    #
    # # Create a new config from the project defaults, and those listed in
    # # conf.cfg
    # _config = ConfigParser.ConfigParser()
    # # Read in the project's defaults
    # _project_default_config = "defaults/{}.cfg".format(_project)
    # if os.path.isfile(_project_default_config):
    #     _config.readfp(pkg_resources.resource_stream(__name__, _project_default_config))
    # else:
    #     _config.readfp(pkg_resources.resource_stream(__name__, 'defaults/default.cfg'))
    # _config.read(['conf.cfg'])
    #
    return _project, _config

project, _config = collect_project_and_config()

# Parse the config and pull in sphinx conf.py settings
project = _config.get('project')
release = _config.get('release')
version = _config.get('version')
author = _config.get('author')
copyright = _config.get('copyright')

needs_sphinx = _config.get('needs_sphinx', '1.0')
exclude_patterns = _config.get('exclude_patterns', [])
extension = _config.get('extensions', [])
language = _config.get('language', None)
master_doc = _config.get('master_doc', 'index')
pygments_style = _config.get('pygments_style', 'sphinx')
source_suffix = _config.get('source_suffix', '.rst')
templates_path = _config.get('templates_path', ['_templates'])
todo_include_todos = _config.get('todo_include_todos', False)
intersphinx_mapping = {
    'python': ('https://docs.python.org/', None),
}

html_extra_path = _config.get('html_extra_path', [])
html_favicon = _config.get('html_favicon', 'favicon.ico')
html_logo = _config.get('html_logo', '_static/lf-logo-small.png')
html_sidebars = _config.get('html_sidebars', {'**': ['localtoc.html', 'relations.html'],})
html_static_path = _config.get('html_static_path', ['_static'])
html_theme = _config.get('html_theme', 'bootstrap')
html_theme_options = _config.get('html_theme_options', {
    'bootswatch_theme': "cerulean",
    'navbar_sidebarrel': False,
    'source_link_position': "footer",
})
html_theme_path = _config.get('html_theme_path', sphinx_bootstrap_theme.get_html_theme_path())
htmlhelp_basename = _config.get('htmlhelp_basename', 'LFDocsConf')
