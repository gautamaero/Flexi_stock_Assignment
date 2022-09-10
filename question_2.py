# -*- coding: utf-8 -*-
"""
Created on Sat Sep 10 18:08:39 2022

@author: mechaerogautam
"""

import numpy as np
import cv2


img1=cv2.imread("input.jpg")
img1 = cv2.resize(img1, img1.shape[1::-1])


img2=cv2.imread("mask.png")
img2 = cv2.resize(img2, img1.shape[1::-1])

exit_condition = 1
  
while (exit_condition) :
  
    alpha = float(input("Enter alpha value:")) 
    
    #  Alpha blending is process of combining one image with a background to create the appearance of partial or full
  
    blended_img = cv2.addWeighted(img1, alpha , img2, 1-alpha, 0.1)
  
    cv2.imwrite('result1.png', blended_img )
  
    img3 = cv2.imread('result1.png')
  
    cv2.imshow("alpha blending 1",img3)
  
    cv2.waitKey(0)
  
    exit_condition = int(input("Enter 1 to continue and 0 to exit:"))

