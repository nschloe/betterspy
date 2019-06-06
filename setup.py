# -*- coding: utf-8 -*-
#
import os
import codecs

from setuptools import setup, find_packages

# https://packaging.python.org/single_source_version/
base_dir = os.path.abspath(os.path.dirname(__file__))
about = {}
with open(os.path.join(base_dir, "betterspy", "__about__.py"), "rb") as f:
    exec(f.read(), about)


def read(fname):
    return codecs.open(os.path.join(base_dir, fname), encoding="utf-8").read()


setup(
    name="betterspy",
    version=about["__version__"],
    author=about["__author__"],
    author_email=about["__author_email__"],
    packages=find_packages(),
    package_data={"betterspy": ["data/journals.json"]},
    description="Show sparsity pattern of sparse matrices",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    url=about["__website__"],
    license=about["__license__"],
    platforms="any",
    install_requires=["matplotlib", "numpy", "purepng", "scipy"],
    classifiers=[
        about["__status__"],
        about["__license__"],
        "Intended Audience :: Science/Research",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Topic :: Scientific/Engineering",
        "Topic :: Utilities",
    ],
    entry_points={"console_scripts": ["betterspy = betterspy.cli:main"]},
)
