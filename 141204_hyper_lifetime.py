from __future__ import division
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

""" File: discounting approaches to uncertain lifetime
aim - to investigate which dicsounting approach leads to highest lifetime 
income under different income shocks - normal shocks or fatter tails?

needs:
economic:
    utility function
    budget constraint
    discount functions - expo, hyper, quasi-hyper?
   income paths - known, random: normal shocks, fat-tail shocks
computing:
    solution method?
    run iterations 1000 times?
    what to store? results from each round (see coin example - ex5.py)
    evolutionary stability?
"""

