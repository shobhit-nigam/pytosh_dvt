"""
sample module

has an important function add,

>>> add(10, 20)
30
"""

def add(la, lb):
    """
    return addition of two positive numbers
    >>> add(10, -1)
    Traceback (most recent call last):
        ...
    ValueError: la and lb must be positive
    """
    if la>0 and lb>0:
        lc = la+lb
    else:
        raise ValueError("la and lb must be positive")
    return lc

if __name__ == '__main__':
    import doctest
    doctest.testmod()
