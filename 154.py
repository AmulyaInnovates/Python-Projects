# -*- coding: utf-8 -*-
"""
Created on Sun Jun 12 11:05:21 2022

@author: Ashish Gupta
"""

import matplotlib.pyplot as plt

data = [[10,10,10,10,10,10,10,10,10, 5,10,10,10],
       [10,10,10,10,10,10,10,10,9, 6, 5,10,10],
       [10,10,10,10,10,10,10, 9,9, 9, 6, 5,10],
       [10,10,10,10,10,10, 9, 9,1, 9, 9, 6, 5],
       [10,10,10,10,10, 9, 9, 9,9, 9, 9, 6, 5],
       [10,10,10,10, 9, 9, 9, 9,1, 9, 9, 6, 5],
       [10,10,10, 9, 9, 9, 9, 9,9, 9, 6, 5, 5],
       [10,10, 9, 9, 9, 9, 1, 9,9, 9, 6, 5, 5],
       [10,9, 1, 9, 1, 9, 9, 9,9, 6, 5, 5,10],
       [5,6, 9, 9, 9, 9, 9, 9,9, 6, 5, 10,10],
       [10,5, 6, 6, 6, 6, 6, 6, 6, 5,10, 10,10],
       [10,10,5, 5, 5, 5, 5, 5, 5, 10,10, 10,10]]

plt.imshow(data, cmap="nipy_spectral")
plt.show()