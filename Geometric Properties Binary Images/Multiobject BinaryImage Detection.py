# -*- coding: utf-8 -*-
"""
Created on Thu Dec 23 23:22:34 2021

@author: otz55
"""

#video url
#Segmenting Binary Images | Binary Images
#https://www.youtube.com/watch?v=2ckNxEwF5YU&list=PL2zRqk16wsdr9X5rgF-d0pkzPdkHZ4KiT&index=17

#A sample code demonstration of binary image segmentation
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import math

#A sample class to classify different group
class Group:

    default = None

    val = 0
    size = 0
    
    def __init__(self, num):
        self.val = num
        self.size = 1
    
    #get group's characteristics instance
    def __getDefault(self, i : Group):
        temp = i
        while temp.default != None:
            temp = temp.default
        
        return temp
    
    #check if 2 groups belong to the same group, log(n) performance
    def isSameGroup(self, i : Group):
        return self.__getDefault(self) == self.__getDefault(i)
    
    #merge two groups to same group, log(n) performance
    def merge(self, i : Group):
        myDefault = self.__getDefault(self)
        iDefault = self.__getDefault(i)
        
        #merge smaller group to larger group
        if myDefault != iDefault:
            if myDefault.size > iDefault.size:
                iDefault.default = myDefault
            else:
                myDefault.default = iDefault
                
            
    

imgArr = np.asarray(Image.open('binaryImage4.bmp')).astype(np.float32)

#flip image from (height, width) shape to (width, height) shape
imgArr = imgArr.T

#label image
#expand width by 1 and height by 1 to avoid out of index problem
segmentationImg = np.zeros((imgArr.shape[0] + 1, imgArr.shape[1] + 1))
counter = 0
labelTable = {}
for x in range(0, eimgArr.shape[0]):
    for y in range(0, eimgArr.shape[1]):
        
        #b(x, y) = 1
        if imgArr[x, y] == 1:
            #if left, top and diagonal are unlabelled
            if segmentationImg[x - 1, y - 1] == 0 and segmentationImg[x - 1, y] == 0 and segmentationImg[x, y] == 0:
                segmentationImg[x, y] = counter
                labelTable[]
                counter += 1
                
            #if diagonal is labelled
            elif segmentationImg[x - 1, y - 1] != 0:
                segmentationImg[x, y] = segmentationImg[x - 1, y - 1]
            
            #if top and left are labelled, then top and left are equivalence
            elif segmentationImg[x - 1, y] != 0 and segmentationImg[x, y - 1] != 0 and segmentationImg[x - 1, y] != segmentationImg[x, y - 1]:
                
                