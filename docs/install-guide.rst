.. _lfdocs-conf-install:

Install Guide
=============

Follow these steps to install lfdocs-conf:

#. Add lfdocs-conf to your requirements.txt
#. Create the docs directory in the root of your repo
#. Create docs/conf.py with the following contents::

     from docs_conf.conf import *

   .. note::

      This is the absolute minimum configuration for this file. Further
      configurations can be found in more detail in the conf.py documentation
      here.

#. Create docs/conf.yaml with the following contents::

     project_cfg: PROJECT

   Replace PROJECT with the name of a project configuration for your top-level
   project. Eg. acumos, onap, opendaylight, opnfv, etc... A list of valid
   projects can be found here. If you are a new project and do not yet have a
   defaults file then please propose a patch to this project.

   .. note::

      This is the absolute minimum configuration necessary to get this going
      further documentation regarding the conf.yaml file can be found here.

#. Create docs/index.rst with the following contents::

     My Project
     ==========

     Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod
     tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim
     veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea
     commodo consequat. Duis aute irure dolor in reprehenderit in voluptate
     velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat
     cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id
     est laborum.

   .. note::

      This is the absolute minimum configuration to get a docs page generated
      for your project. What you do from here is entirely up to you. Please
      refer to the `Sphinx reStructuredText Primer
      <http://www.sphinx-doc.org/en/stable/rest.html>`_.

#. (Optional) Copy project logo to docs/_static/logo.png

   .. note::

      The logo should be a small 64x64 png image.

#. (Optional) Copy a favicon to docs/_static/favicon.ico
