"""
Entity movement subsystem for alife program

I K Stead, 12-09-2012
"""
import random

def random_pos(xlim, ylim):
    x = random.randint(1, xlim)
    y = random.randint(1, ylim)
    return (x, y)
