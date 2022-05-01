"""Implementation of the function 'load_model'."""
from os import getenv
from pickle import load


def load_model(filename=getenv('MODEL_FILENAME')):
    """Loads the model from the local disk"""
    with open(filename, 'rb') as file:
        loaded_model = load(file)
        return loaded_model
