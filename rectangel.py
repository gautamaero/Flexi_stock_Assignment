# -*- coding: utf-8 -*-
"""
Created on Sat Sep 10 17:23:51 2022

@author: mechaerogautam
"""

import numpy as np
            
            
def bbox1(rectangle):
    a = np.where(rectangle != 0)
    bbox = np.min(a[0]), np.max(a[0]), np.min(a[1]), np.max(a[1])
    return f'x: {bbox[0]}, y: {bbox[2]}, height: {bbox[3]}, width: {bbox[1]}'           

###

rectangle=np.array([[0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0],
                    [0,0,0,1,0,0,0],
                    [0,0,0,0,0,1,0],
                    [0,0,0,0,1,0,0]])

n_rows,n_columns=rectangle.shape 

print(n_rows,n_columns)
print(bbox1(rectangle))

