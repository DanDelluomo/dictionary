#!/usr/bin/env python

# Import Standard Libary Packages
import pathlib
import pickle

pickle_path = pathlib.Path(__file__).absolute().parents[1] / "data" / "dict_pkl"

def get_dict() -> dict:
    with open(pickle_path, 'rb') as pickle_dict:
        return pickle.load(pickle_dict)