from setuptools import setup, find_packages
from ASHURE.__init__ import __version__, __author__, __email__, __name__

def read(path):
    with open(path, "r") as f:
        out = f.read()
    return out

long_description = read("README.md")

setup(
    name=__name__,
    version=__version__,
    license="LGPL-3",
    author=__author__,
    author_email=__email__,
    maintainer=__author__,
    maintainer_email=__email__,
    description="Python package for clustering and consensus error corrections of reads from nanopore sequencing",
    long_description=long_description,
    long_description_content_type="text/markdown",
    zip_safe=False,
    packages=find_packages(include=[__name__]),
    include_package_data=True,
    python_requires=">=3.7",
    install_requires=open("requirements.txt").read().strip().split("\n"),
    setup_requires=open("requirements.txt").read().strip().split("\n"),
    url="https://github.com/zchen15/ASHURE2",
    keywords="nanopore, clustering, NGS, error correction",
    entry_points={
        "console_scripts": [__name__+'='+__name__+'.main:main'],
    },
    classifiers=[
        "Environment :: Console",
        "Framework :: Jupyter",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: LGPL-3",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.7",
        "Topic :: Scientific/Engineering :: Bio-Informatics",
        "Topic :: Utilities",
    ],
)
