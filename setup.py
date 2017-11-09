"""
Setup for Docs Configuration
"""
from setuptools import setup, find_packages

setup(
    name='docs_conf',
    packages=['docs_conf'],
    version='0.1.0',
    author="Trevor Bramwell",
    author_email="tbramwell@linuxfoundation.org",
    url="https://gerrit.linuxfoundation.org/docs-conf",
    package_data={
        'docs_conf': ['defaults/*']
    },
)
