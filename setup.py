"""
Setup for Docs Configuration
"""
__author__ = 'Linux Foundation Releng'
__summary__ = 'Linux Foundation DocsConf'
__version__ = '0.2.0-dev'


from setuptools import setup, find_packages


with open('requirements.txt') as f:
    install_reqs = f.read().splitlines()


setup(
    name='lfdocs_conf',
    packages=['docs_conf'],
    version=__version__,
    author=__author__,
    author_email="releng@linuxfoundation.org",
    url="https://gerrit.linuxfoundation.org/docs-conf",
    package_data={
        'docs_conf': ['defaults/*']
    },
    install_requires=install_reqs
)
