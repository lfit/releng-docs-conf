LF Docs Config
==============

The purpose of this project is to allow LF projects a centralized location for
storing common project configuration.

Though the project is specific to LF projects, it's aim is to
be general enough for other projects to use as an easy mechanism for
managing the same Sphinx conf.py file across many repositories.

Quick Start
-----------

First start by installing this project, perferrably in a virtualenv with
the following command::

    pip install docs-conf

Then at the same location as your Sphinx conf.py file in your docs
directory, create a conf.yaml file, containing at a minimum::

    ---
    project_cfg=myproject

The conf.py file should contain at minimum::

    from docs_conf import *

This will enable conf.py to contain (at the runtime of sphinx-build) all
defaults listed in **docs_conf/defaults/defaults.yaml**. If project
defaults for 'myproject' exist in this repo
(**docs_conf/defaults/myproject.yaml**), they will be loaded and
override the base defaults. Otherwise the basic Sphinx defaults will be
set.

Configuration Inheritance
-------------------------

Because of the way this project is structured, Sphinx defaults are all
inherited from the following sources and merged, with those at the top
of the list taking precedence over those lower down:

#. project/conf.py
#. project/conf.yaml
#. docs_conf/defaults/{project_cfg}.yaml
#. docs_conf/defaults/default.yaml
#. docs_conf/conf.py

The full list of Sphinx configuration settings and their types can be
found here: http://www.sphinx-doc.org/en/stable/config.html

Contributing
------------

Testing
~~~~~~~

TODO
----

- [ ] Define the minimum set of config values to release initial version.
      These can probably come from ODL/OPNFV site conf.py files.

- [ ] Use sane defaults, and don't error out if something is not set.
      Each config needs to be imported gracefully (if it doesn't
      exist, set None or something; similar to dict.get

- [ ] Create own documentation for project detailing use of 'conf.cfg'
      file as some values will require subkeys given that they're
      dictionaries or expect a list of tuples.

- [ ] Setup and document section. The documentation already is organized
      by section, so the config should also contain these section and look
      for their values under them.

      Sections:

        - general (aka sphinx)
        - project
        - i18n
        - html_output
        - apple_help
        - epub_output
        - latex_output
        - text_output
        - manpage_output
        - texinfo_output
        - linkcheck
        - xml
        - cplusplus

- [ ] Configure pre-plugin sections, and reference by plugin listing.
