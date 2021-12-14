"""
Takes data from webppl and adds color to it
"""


# lib
import matplotlib as plot
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib import pylab
import numpy as np
from pylab import *


samples = [{"value":{"tonal_difference":0.2,"headline_obj":1.0653916966635228,"obj_diff":0.16267529724740312}}] # sample data
cmap = cm.get_cmap('gist_rainbow',100)


for i in range(len(samples)):
    ind = int(samples[i]["value"]["obj_diff"]*100) # gets value based on obj diff
    rgba = cmap(ind) # maps to color map
    samples[i]["value"]["color"] = matplotlib.colors.rgb2hex(rgba) # convert to hex
print(samples)