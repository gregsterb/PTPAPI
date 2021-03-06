#!/usr/bin/env python
from setuptools import setup

setup(
    name="PTPAPI",
    version="0.4",
    install_requires=[
        "requests",
        "beautifulsoup4",
        "tempita"
    ],
    extras_require={
        'reseed': ['guessit>=2']
    },
    packages=[
        'ptpapi',
        'ptpapi.sites',
    ],
    scripts=[
        'scripts/ptp',
        'scripts/ptp-reseed',
        'scripts/ptp-reseed-machine',
    ],
)
