# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 11:11:09 2021

@author: Musya
"""

import csv
import os


def writeCsv(list1,list2,list3):
    #os.mkdir('CSV')
    os.chdir('CSV')
    with open('logdata.csv', 'w', newline = '') as csvfile:
        fieldnames = ['Image_name','Steering_angle','Throttle']
        theWriter = csv.DictWriter(csvfile,
                                   fieldnames=fieldnames)
        #theWriter.writeheader()
        for i in range(len(list1)):
            theWriter.writerow({'Image_name':list1[i],
                                'Steering_angle':list2[i],
                                'Throttle':list3[i]}
                               )
            
        print("Data Written:",len(list1))
        