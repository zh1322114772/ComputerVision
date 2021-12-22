# -*- coding: utf-8 -*-
"""
Created on Wed Dec 22 12:53:24 2021

@author: otz55
"""

#video url
#Geometric Properties | Binary Images
#https://www.youtube.com/watch?v=ZPQiKXqHYrM&list=PL2zRqk16wsdr9X5rgF-d0pkzPdkHZ4KiT&index=16

import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from matplotlib.patches import Circle
import math

imgArr = np.asarray(Image.open('binaryImage3.bmp')).astype(np.float32)

#get center
y_pixels = np.arange(0, imgArr.shape[0]).reshape(-1, 1)
x_pixels = np.arange(0, imgArr.shape[1]).reshape(-1, 1)
area = np.ones((1, imgArr.shape[1]), np.float32).reshape(-1, 1)

area_sum = np.sum(np.dot(imgArr, area))
x_bar = np.sum(np.dot(imgArr, x_pixels)) / area_sum
y_bar = np.sum(np.dot(imgArr.T, y_pixels)) / area_sum


#get orientation
x_mesh, y_mesh = np.meshgrid(x_pixels.T, y_pixels.T)

#get a
a_matrix = x_mesh - x_bar
a_matrix = np.power(a_matrix, 2) * imgArr
a = np.sum(a_matrix)
#get c
c_matrix = y_mesh - y_bar
c_matrix = np.power(c_matrix, 2) * imgArr
c = np.sum(c_matrix)

#get b
b_matrix = (x_mesh - x_bar) * (y_mesh - y_bar) * imgArr
b = np.sum(b_matrix)

#get theta
theta1 = math.atan(b/(a - c))/2
theta2 = theta1 + math.pi/2

#get min theta
theta = 0
if ((a - c) * math.cos(2 * theta1)) + (b * math.sin(2 * theta1)) > 0:
    theta = theta1
else:
    theta = theta2

#plot
fig, ax = plt.subplots(1)
ax.set_aspect('equal')
ax.imshow(imgArr)

#draw orientation line
m = math.sin(theta)/math.cos(theta)

for i in range(0, imgArr.shape[1], 10):
    ax.add_patch(Circle((i, (m * (i - x_bar)) + y_bar), 5))


#add circle
cir = Circle((x_bar, y_bar), 10)
ax.add_patch(cir)

plt.show()