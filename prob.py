# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 09:45:53 2015

@author: Administrator
"""

import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

x=[1,1,1,1,1,1,1,1,2,2,2,3,4,4,4,4,5,6,6,6,7,7,7,7,7,7,7,7,8,8,9,9]

# Box Plot
plt.figure()
plt.boxplot(x)
plt.savefig("boxplot.png")

 # Histogram
plt.figure()
plt.hist(x, histtype='bar')
plt.savefig("histogram.png")

 # QQ-Plots
plt.figure()
test_data = np.random.normal(size=1000)
graph1 = stats.probplot(test_data, dist="norm", plot=plt)
plt.show()
plt.savefig("normal-qq-plot.jpg")

plt.figure()
test_data2 = np.random.uniform(size=1000)
graph2 = stats.probplot(test_data2, dist="norm", plot=plt)
plt.show()
plt.savefig("uniform-qq-plot.jpg")