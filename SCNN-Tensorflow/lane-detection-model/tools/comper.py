# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 12:25:01 2020

@author: Mouiad
"""
import cv2
def draw(original,path22):
    f = open(path22, "r")
    for line in f :
        x = []
        y = []
        points = line.split(" ")
        for i in range(0,(len(points)-1),2):
            x.append(points[i])
            y.append(points[i+1])

        for i  in range(0 , len(x)-1):
            #print(x[i] , y[i])
            cv2.line(original, (int(float(x[i])), int(y[i])),(int(float(x[i+1])), int(y[i+1])) , (0,255,0), 8)
        
    #print("--------------------------------------------------------------------------")
    #cv2.waitKey(0)
    cv2.imshow("original",original)
    cv2.waitKey(0)
    f.close()
    return original
output2=open(r"C:\Users\Mouiad\Desktop\Codes-for-Lane-Detection\SCNN-Tensorflow\lane-detection-model\prob2lines\output\vgg_SCNN_DULR_w9\driver_100_30frame\05250541_0314.MP4\00510.lines.txt",'r')
label=open(r"C:\Users\Mouiad\Desktop\Codes-for-Lane-Detection\SCNN-Tensorflow\lane-detection-model\data\CULane\driver_100_30frame\05250541_0314.MP4\00510.lines.txt",'r')
img=cv2.imread(r"C:\Users\Mouiad\Desktop\Codes-for-Lane-Detection\SCNN-Tensorflow\lane-detection-model\data\CULane\driver_100_30frame\05250541_0314.MP4\00510.jpg")
output1=r"C:\Users\Mouiad\Desktop\Codes-for-Lane-Detection\SCNN-Tensorflow\lane-detection-model\prob2lines\output\vgg_SCNN_DULR_w9\driver_100_30frame\00510.lines.txt"
label1=r"C:\Users\Mouiad\Desktop\Codes-for-Lane-Detection\SCNN-Tensorflow\lane-detection-model\data\CULane\driver_100_30frame\05250541_0314.MP4\00510.lines.txt"
Scnn=r"C:\Users\Mouiad\Desktop\Codes-for-Lane-Detection\SCNN-Tensorflow\lane-detection-model\prob2lines\output\vgg_SCNN_DULR_w9\driver_100_30frame\05250541_0314.MP4\00510.lines.txt"
#draw(img,output1)
#draw(img,label1)
def line2lists(output):
    xaxi=[]
    yaxi=[]
    for line in output :
        X=[]
        Y=[]
        points = line.split(" ")
        for i in range(0,(len(points)-1),2):
                X.append(float(points[i]))
                Y.append(float(points[i+1]))
        xaxi.append(X)
        yaxi.append(Y)
    return xaxi
X=line2lists(output2)
XX=line2lists(label)
l=[i[0] for i in X]
ll=[i[0] for i in XX]
print(l)
print(ll)
x=[]
for i in range(len(l)):
    for j in range(len(ll)):
        if abs(l[i]-ll[j])<=30.0:
            print("cv line "+str(i) +" match labels line "+ str(j))
            print(abs(l[i]-ll[j]))
            x.append(j)
            break
L=[0,1,2,3]
sc= [item for item in L if item not in x]
scnn=list(sc)
i=0
file=open("line.txt",'w')
f=open(Scnn,'r')
f1=open(output1,'r')
while i<4:
    if i in scnn:
        file.writelines(f.readline())
        print(i)
    elif i in x:
        file.writelines(f1.readline())
        print(i)
        f.readline()
    i+=1
        
    

