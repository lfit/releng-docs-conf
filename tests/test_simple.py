#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# SPDX-License-Identifier: EPL-1.0
##############################################################################
# Copyright (c) 2017-2018 The Linux Foundation and others.
#
# All rights reserved. This program and the accompanying materials
# are made available under the terms of the Eclipse Public License v1.0
# which accompanies this distribution, and is available at
# http://www.eclipse.org/legal/epl-v10.html
##############################################################################
"""
Docs Conf Tests
"""
import pytest

conf_yaml = """
---
project: myproject
author: Pythonista
"""

conf_yaml1 = """
---
project: mypro
author: Python
"""

def test_config(confyaml):
    """
    Assert some basic assumption about how configurations are pulled in
    """
    config = confyaml(conf_yaml)
    assert config.project == 'myproject'
    assert config.author == 'Pythonista'

    config = confyaml(conf_yaml1)
    assert config.project == 'mypro'
    assert config.author == 'Python'

@pytest.mark.skip(reason="Not implemented")
def test_defaults(confyaml):
    """
    Test the defaults are set and the only thing required is a conf.py
    w/import *
    """
    # TODO
    assert True

@pytest.mark.skip(reason="Not implemented")
def test_project_override(config):
    """
    Test that setting sphinx.project pulls in the project specific
    defaults
    """
    # TODO
    assert True

@pytest.mark.skip(reason="Not implemented")
def test_theme_import(config):
    """
    Test setting sphinx.html_theme_module imports the correct theme
    """
    # TODO
    pass
