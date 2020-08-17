#Esto es una prueba


# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 16:00:26 2020

@author: pjac2
"""

# from __future__ import division #omit for python 3.x
import numpy as np
import pandas as pd
import sys
import os
from scipy import stats
import math
from math import *
import seaborn as sns

data_One = pd.read_stata('PythonDataSt.dta')

data_One["ptj_portafolio_a2016"] = data_One["ptj_portafolio_a2016"].fillna(0)
data_One["ptj_prueba_a2016"] = data_One["ptj_prueba_a2016"].fillna(0)

count_nan = data_One["ptj_portafolio_a2016"].isna().sum()
count_nan_1 = data_One["ptj_prueba_a2016"].isna().sum()

catp1 = data_One['ptj_portafolio_a2016'].to_numpy()

catp2 = data_One['ptj_prueba_a2016'].to_numpy()

years = data_One['experience'].to_numpy()




mu, sigma = 0, 1 # mean and standard deviation
misj = len(catp1)
enormal = np.random.normal(mu, sigma, misj)
        
#ojo con profes no tienen alguno de estos ptjes
p0 = np.zeros(catp1.shape)
p0 = np.where((catp1 == 0),catp2, p0)
p0 = np.where((catp2 == 0),catp1, p0)
p0 = np.where((catp1 != 0) & (catp2 != 0) ,(catp1 + catp2)/2, p0)

p = []

alphas = [[0.5,0.5,-0.05,0.05],
		[0.5,0.5,-0.05,-0.05]]


for j in range(2):
    p.append(alphas[j][0]*p0 + \
             alphas[j][1]*enormal + \
                 alphas[j][2]*np.square(enormal) + \
                     alphas[j][3]*years)


a, b = p
print(a)
print(b)


ef = np.random.randn(misj)

print("Quiero saber si dunciona la rama")
print("Hola mundo")




