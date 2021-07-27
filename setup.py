#!/usr/bin/env python

# Copyright 2021 Daniel E. Dell'uomo

import pathlib
from setuptools import setup

HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()

setup(
    name="english_dictionary",
    version="1.0.24",
    description="In-memory dictionary of 100 thousand English words",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/DanDelluomo/dictionary",
    author="Daniel E. Dell'uomo",
    author_email="dandelluomo@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["english_dictionary"],
    package_dir={'english_dictionary': 'english_dictionary'},
    package_data={'english_dictionary': ['data/*']},
    include_package_data=True,
    install_requires=[
        "requests",
        "bs4",
    ],
    entry_points={
        "console_scripts": [
            "dictionary=english_dictionary.scripts.read_pickle:get_dict"
        ]
    },
)
