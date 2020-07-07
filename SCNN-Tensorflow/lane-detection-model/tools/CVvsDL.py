# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 13:36:04 2020

@author: Mouiad
"""

import cv2
import glob
import matplotlib.pyplot as plt
import os
from time import sleep
from advanced_lane import *
def comper(path):
     file=open(r"C:\Users\Mouiad\Desktop\Codes-for-Lane-Detection\SCNN-Tensorflow\lane-detection-model\demo_file\test_img.txt","w")
     image_name="../"+path[86:]

     image_name2=path[97:]
     name=path[-9:]
     name1=path[-8:]
     file2=open(r"C:\Users\Mouiad\Desktop\Codes-for-Lane-Detection\SCNN-Tensorflow\lane-detection-model\data\CULane\list\test.txt","w")
     file.write(image_name)
     file2.writelines(image_name2)
     sleep(5)
     cv=r"C:\Users\Mouiad\Desktop\Codes-for-Lane-Detection\SCNN-Tensorflow\lane-detection-model\Visual_output\cv\image\\"+name
     dl=r"C:\Users\Mouiad\Desktop\Codes-for-Lane-Detection\SCNN-Tensorflow\lane-detection-model\Visual_output\Dl\image\\"+name1
     print("SCNN is Ready to in to the network")
     #import test_lanenet as t
     for img_name in glob.glob(path):
            img = cv2.imread(img_name)
            init_lines(img.shape[0])
            img2,L,R = pipeline1(img)
            plt.imsave(r"C:\Users\Mouiad\Desktop\Codes-for-Lane-Detection\SCNN-Tensorflow\lane-detection-model\Visual_output\cv\image\\"+name,img2)
            image_name=img_name[-9:]
            img2=cv2.cvtColor(img2, cv2.COLOR_RGB2BGR)
            #plt.figure(figsize = (10,5))
            #plt.imshow(img2)
            parent_path = os.path.dirname(path)[98:]
            parent_path = parent_path.replace('/', '\\')
            directory = os.path.join(r"C:\Users\Mouiad\Desktop\Codes-for-Lane-Detection\SCNN-Tensorflow\lane-detection-model\experiments\predicts", 'vgg_SCNN_DULR_w9', parent_path)
            if not os.path.exists(directory):
                    os.makedirs(directory)
            file_exist = open(os.path.join(directory, os.path.basename(path)[:-3] + 'CVexist.txt'), 'w')
            for cnt_img in range(1):
              cv2.imwrite(os.path.join(directory, os.path.basename(path)[:-4] + '_' + str(cnt_img + 2) + 'cv_avg.png'),L)
              cv2.imwrite(os.path.join(directory, os.path.basename(path)[:-4] + '_' + str(cnt_img + 3) + 'cv_avg.png'),R)
            file_exist.write('0 ')
            if ones_or_zeros_for_Right()==True:
                file_exist.write('1 ')
            else:
                file_exist.write('0 ')
            if ones_or_zeros_for_Left()==True:
                file_exist.write('1 ')
            else:
                file_exist.write('0 ')
            file_exist.write('0 ')
            file_exist.close()
     print("CV is Ready to shown")
     return cv,dl

     #fig=plt.figure(figsize=(8, 8))
     #fig.add_subplot(1, 2, 0)
     #plt.imshow(img2)
     