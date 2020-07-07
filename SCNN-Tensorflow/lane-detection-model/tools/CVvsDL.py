# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 13:36:04 2020

@author: Mouiad
"""

import cv2
import glob
import matplotlib.pyplot as plt'
import os
def comper(path):
     for img_name in glob.glob(path):
            img = cv2.imread(img_name)
            init_lines(img.shape[0])
            img2,L,R = pipeline1(img)
            image_name=img_name[-9:]
            img2=cv2.cvtColor(img2, cv2.COLOR_RGB2BGR)
            #plt.figure(figsize = (10,5))
            #plt.imshow(img2)
            parent_path = os.path.dirname(path)[98:]
            parent_path = parent_path.replace('/', '\\')
            directory = os.path.join(r"C:\Users\Mouiad\Desktop\Codes-for-Lane-Detection\SCNN-Tensorflow\lane-detection-model\experiments\predicts", 'vgg_SCNN_DULR_w9', parent_path)
            if not os.path.exists(directory):
                    os.makedirs(directory)
            file_exist = open(os.path.join(directory, os.path.basename(filename)[:-3] + 'exist.txt'), 'w')
            for cnt_img in range(1):
              cv2.imwrite(os.path.join(directory, os.path.basename(filename)[:-4] + '_' + str(cnt_img + 2) + '_avg.png'),L)
              cv2.imwrite(os.path.join(directory, os.path.basename(filename)[:-4] + '_' + str(cnt_img + 3) + '_avg.png'),R)
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