#!/usr/bin/env python

# Copyright 2021 Daniel E. Dell'uomo

import pathlib
from setuptools import setup

HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()

setup(
    name="english_dictionary",
    version="1.0.0",
    description="In-memory dictionary of one hundred thousand English words",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/DanDelluomo/dictionary",
    author="Daniel E. Dell'uomo",
    author_email="dandelluomo@gmail.com".
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],

)
