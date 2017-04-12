#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 12:27:21 2017

@author: ziaulchoudhury
"""

import matplotlib.pyplot as plt  
import numpy as np  
 

b = []
b2 = []
l =[]
l2 = [] 
l3=[]
b3=[]

#-----------First Image-------------#        
img = plt.imread('2015.png')	#Read in image from 2015.png
plt.imshow(img)			#Load image into matplotlib
height = img.shape[0]
width = img.shape[1]
newImage = np.zeros((height,width,3))
for i in range(height):
	for j in range(width):
         l.append(i)
         newImage[i,j,0] = img[i,j,0] # assaging red value
         newImage[i,j,0] = img[i,j,1]
         newImage[i,j,2] = img[i,j,2]
         if newImage[i,j,2] > .90:    # taking the bule value>.90 to measure the water
             b.append(newImage[i,j,2])

plt.imshow(newImage)	#Open window to show image (close to continue)
plt.title('Image One')
plt.show() 
plt.imsave('new2015.png',newImage)

#-----------Second Image-------------# 
img2 = plt.imread('2016.png')	#Read in image from 2016.png
plt.imshow(img2)			#Load image into matplotlib
height2 = img2.shape[0]
width2 = img2.shape[1]
newImage2 = np.zeros((height2,width2,3))
for i2 in range(height2):
	for j2 in range(width2):
         l2.append(i2)
         newImage2[i2,j2,1] = img2[i2,j2,0]# assaging green value
         newImage2[i2,j2,1] = img2[i2,j2,1]
         newImage2[i2,j2,0] = img2[i2,j2,2]
         if newImage2[i2,j2,0] > .90:    # taking the red value>.90 to measure the water
             b2.append(newImage2[i2,j2,2])

plt.imshow(newImage2)	#Open window to show image (close to continue)
plt.title('Image Two')
plt.show() 
plt.imsave('new2016.png',newImage2)

#-----------Calculations-------------# 
print('Number of RED Pixes: ',len(b2),', Number of All Pixels: ',len(l2))
print('Number of Blue Pixes: ',len(b),', Number of All Pixels: ',len(l))
 
p1 = len(b)/(len(l)/100)      # using the length of list to measure how much area contains water
print('Percentage of river/lake', p1)

p2 = len(b2)/(len(l2)/100)    # using the length of list to measure how much flooded area contains water inculding rivers
print('Percentage of water area after the flood includeing river/lake: ', p2)

p3 = (p2 - p1)  # actual are that were flooded 
print('Actual percentage of land that were flooded', p3)

from PIL import Image       # blending imgae to show rivers and flooded area
background = Image.open("new2016.png")
foreground = Image.open("new2015.png")
Image.blend(background,foreground, 0.5).show()
