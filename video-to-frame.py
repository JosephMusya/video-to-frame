# -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 23:10:00 2021

@author: Musya
"""

import cv2
import sys
import os
from csvfile import writeCsv

os.chdir('DATA')
os.mkdir('IMG')
os.mkdir('CSV')
os.chdir('IMG')

path = os.getcwd()
print(path)
#sys.exit()
count = 0
s = 0
t = 0
cap = cv2.VideoCapture(0)

images = []
steering =  []
throttle = []
def captureData():
    global count
    global t
    global s
    while True: 
        count = count + 1
        t = t + .5
        s = round(((t/4)*.34),3)
        
        name = str(count) + '.jpeg'
        name = str(os.path.join(path,name))
        
        _,frame = cap.read()  
        cv2.imwrite(name,frame)
        cv2.imshow("frame",frame)
        
        images.append(name)
        steering.append(s)
        throttle.append(t)
        
        if cv2.waitKey(1) == ord('q'):
            break
        print(name)
        
    writeCsv(images, steering, throttle)
captureData()
    
    
    
    