"""
Docs Conf Tests
"""
import importlib
import os
import pytest
import sys

@pytest.fixture()
def config(tmpdir):
    """
    Create a basic conf.py and conf.cfg file for each test
    """
    # Create the base 'conf.py'
    confpy = tmpdir.join('conf.py')
    confpy.write("from docs_conf import *")

    # Create conf.cfg file with test defaults
    # TODO: Make this dynamic so each test can set their own conf.cfg
    # config.
    confcfg = tmpdir.join('conf.yaml')
    confcfg.write("---\nproject: myproject\nauthor: Pythonista")

    # Change to the tmpdir location so relative file lookups succeed
    os.chdir(str(tmpdir))

    # Import the 'conf.py' file
    sys.path.append(str(tmpdir))
    conf_module = importlib.import_module('conf')

    return conf_module

def test_config(config):
    """
    Assert some basic assumption about how configurations are pulled in
    """
    assert config.project == 'myproject'
    assert config.author == 'Pythonista'
    #assert 'latex_documents' in dir(config)

def test_defaults(config):
    """
    Test the defaults are set and the only thing required is a conf.py
    w/import *
    """
    # TODO
    assert True

def test_project_override(config):
    """
    Test that setting sphinx.project pulls in the project specific
    defaults
    """
    # TODO
    assert True

def test_theme_import(config):
    """
    Test setting sphinx.html_theme_module imports the correct theme
    """
    # TODO
    pass
