""" Stats distributions tests"""
from scipy.stats import norm, cauchy
import matplotlib.pyplot as plt

fig, ax = plt.subplots(1, 1)
mean, var, skew, kurt = cauchy.stats(moments='mvsk')
print kurt

mean_n, var_n, skew_n, kurt_n = norm.stats(moments='mvsk')
print mean_n
print var_n, skew_n, kurt_n