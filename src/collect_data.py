"""Implementation of the function 'collect_data'."""
from numpy import array, float64


def collect_data(container: dict, fields):
    """Collects the data in a vector np.array providing the fields, if no data
    is found returns None"""
    buffer = [[]]
    for field in fields:
        if field not in container:
            return
        buffer[0].append(container[field])

    return array(buffer, dtype=float64).reshape(-1, len(fields))
