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

#A sample class to classify different group
class Group:

    default = None

    val = 0
    size = 0
    
    def __init__(self, num):
        self.val = num
        self.size = 1
    
    #get group's characteristics instance
    def getDefault(self, i):
        temp = i
        while temp.default != None:
            temp = temp.default
        
        return temp
    
    #check if 2 groups belong to the same group, log(n) performance
    def isSameGroup(self, i):
        return self.getDefault(self) == self.getDefault(i)
    
    #merge two groups to same group, log(n) performance
    def merge(self, i):
        myDefault = self.getDefault(self)
        iDefault = self.getDefault(i)
        
        #merge smaller group to larger group
        if myDefault != iDefault:
            if myDefault.size > iDefault.size:
                iDefault.default = myDefault
                myDefault.size += iDefault.size
            else:
                myDefault.default = iDefault
                iDefault.size += myDefault.size

    

imgArr = np.asarray(Image.open('binaryImage4.bmp')).astype(np.float32)

#flip image from (height, width) shape to (width, height) shape
imgArr = imgArr.T

#label image
#expand width by 1 and height by 1 to avoid out of index problem
segmentationImg = np.zeros((imgArr.shape[0] + 1, imgArr.shape[1] + 1))
counter = 0
labelTable = {}
for y in range(0, imgArr.shape[1]):
    for x in range(0, imgArr.shape[0]):
        
        #b(x, y) = 1
        if imgArr[x, y] == 1:
            #if left, top and diagonal are unlabelled
            if segmentationImg[x, y] == 0 and segmentationImg[x, y + 1] == 0 and segmentationImg[x + 1, y] == 0:
                segmentationImg[x + 1, y + 1] = counter
                labelTable[counter] = Group(counter)
                counter += 1
                
            #if diagonal is labelled
            elif segmentationImg[x, y] != 0:
                segmentationImg[x + 1, y + 1] = segmentationImg[x, y]
            
            #if top and left are labelled, then top and left are equivalence
            elif segmentationImg[x, y + 1] != 0 and segmentationImg[x + 1, y] != 0 and segmentationImg[x, y + 1] != segmentationImg[x + 1, y]:
                 
                #merge two groups
                if not labelTable[segmentationImg[x, y + 1]].isSameGroup(labelTable[segmentationImg[x + 1, y]]):
                    labelTable[segmentationImg[x, y + 1]].merge(labelTable[segmentationImg[x + 1, y]])
                
                segmentationImg[x + 1, y + 1] = segmentationImg[x, y + 1]
            
            #if top is labelled, then label b(x, y) as same as top
            elif segmentationImg[x + 1, y] != 0:
                segmentationImg[x + 1, y + 1] = segmentationImg[x + 1, y]
                
            #if left is labelled, then label b(x, y) as same as left
            elif segmentationImg[x, y + 1] != 0:
                segmentationImg[x + 1, y + 1] = segmentationImg[x, y + 1]
                
#define group dictionary
counter = 0
labelDict = {}

for key, group in labelTable.items():
    labelDict[key] = group.getDefault(group).val
    print(labelDict[key], key)
    
#re-assign values
for y in range(1, imgArr.shape[1]):
    for x in range(1, imgArr.shape[0]):
        if segmentationImg[x, y]!= 0:
            segmentationImg[x, y] = labelDict[segmentationImg[x, y]]
        else:
            segmentationImg[x, y] = 255



plt.imshow(segmentationImg)
plt.show()
plt.imshow(imgArr)
plt.show()
