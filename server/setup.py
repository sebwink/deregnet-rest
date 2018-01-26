# coding: utf-8

import sys
from setuptools import setup, find_packages

NAME = "deregnet_rest"
VERSION = "1.0.0"

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["connexion"]

setup(
    name=NAME,
    version=VERSION,
    description="DeRegNet REST API",
    author_email="deregnet@informatik.uni-tuebingen.de",
    url="",
    keywords=["Swagger", "DeRegNet REST API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['swagger/swagger.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['deregnet_rest=deregnet_rest.__main__:main']},
    long_description="""\
    DeRegNet REST API 
    """
)

