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
