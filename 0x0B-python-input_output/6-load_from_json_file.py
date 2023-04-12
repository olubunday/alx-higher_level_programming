#!/usr/bin/python3
"""Contains the function load_from_json_file that creates an object from a “JSON file”"""


import json


def load_from_json_file(filename):
    """crate and object from a "JSON file" """
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
