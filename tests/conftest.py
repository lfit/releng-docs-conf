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
Fixtures for docs-conf testing

This file is explicilty 'conftests.py' as that is where pytest defines
automatically imported fixtures should live.
"""
import importlib
import os
import pytest
import sys

@pytest.fixture(scope='function')
def write_confpy(tmpdir, autouse=False):
    """
    Create a basic conf.py and conf.yaml file for each test
    """
    # Create the base 'conf.py'
    confpy = tmpdir.join('conf.py')
    confpy.write("from docs_conf.conf import *")

    return tmpdir

@pytest.fixture(scope='function')
def confyaml(write_confpy, autouse=False):
    """
    Create a conf.yaml file from the string passed to confyaml_file
    """
    def create_conf_yaml(conf_yaml_file):
        tmpdir = write_confpy

        if conf_yaml_file is not 'None':
            # Create conf.yaml file with test defaults
            conf_yaml = tmpdir.join('conf.yaml')
            conf_yaml.write(conf_yaml_file)

        # Change to the tmpdir location so relative file lookups succeed
        os.chdir(str(tmpdir))

        # Import the 'conf.py' file
        sys.path.append(str(tmpdir))

        conf_module = importlib.import_module('conf')

        return conf_module

    return create_conf_yaml

