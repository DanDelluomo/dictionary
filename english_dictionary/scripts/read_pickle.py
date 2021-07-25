#!/usr/bin/env python

# Import Standard Libary Packages
import pathlib
import pickle

def get_dict() -> dict:
    with open('dict_pkl', 'rb') as pickle_dict:
        return pickle.load(pickle_dict)