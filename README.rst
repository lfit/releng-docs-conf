Sphinx Docs Config
==================

To use this file a project should create a conf.cfg file in the same
directory as their conf.py. Conf.py should contain::

    from docs-conf import *

The conf.cfg file should contain at minimum::

    [sphinx]
    project=myproject

And if defaults for 'myproject' exist, they will be loaded from this
package, otherwise the basic Sphinx defaults will be
set.

Parsing of configs follows this list::

    #.docs-conf/__init__.py
    #.project/conf.cfg (single-value)
    #.docs-conf/defaults/default.cfg or docs-conf/defaults/project.cfg
    #.project/conf.cfg (all values)
    #.project/conf.py

conf.py structure and documentation:
  http://www.sphinx-doc.org/en/stable/config.html

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
