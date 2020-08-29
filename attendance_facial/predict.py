import sys
sys.path.append('~/.local/lib/python3.5/site-packages')
sys.path.remove('/opt/ros/kinetic/lib/python2.7/dist-packages')

import numpy as np
import matplotlib.pyplot as plt
import os
import cv2
from tqdm import tqdm
from numpy import argmax


DATADIR = '/home/sammy-ros/attendance_facial/datasets'
CATEGORY=[]
for L in os.listdir(DATADIR): 
    CATEGORY.append(L)
print(CATEGORY)

present_list = []


face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt_tree.xml')


rec = cv2.face.LBPHFaceRecognizer_create()    
rec.read('trainingData.yml')                                       



# for prediction from image : 

'''img = cv2.imread('IMG_20200623_180747.jpg')
img = cv2.resize(img, (2*640,2*360))
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)                                
faces = face_cascade.detectMultiScale(gray)
print(len(faces))

totalConf = 0.0
faceRec = 0
for (x, y, w, h) in faces:
    cv2.rectangle(img,(x,y),(w+x,y+h),(0,0,255),6)
    id, conf = rec.predict(gray[y:y+h, x:x+w])    
    print(id,conf)
    if conf >= 0 and conf <=95:
        
        profile = CATEGORY[id-1]
        print(profile)
        cv2.putText(img, profile,(x+w,y),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,255),2,cv2.LINE_AA)
while True:
	cv2.imshow('ss',img)
	if cv2.waitKey(5) and 0xFF == 27:
	    break

'''
cap =cv2.VideoCapture(-1)
cap =cv2.VideoCapture('test_video_HD 720p.mp4')

boxlimit = 700

while True:
    ret,frame = cap.read()
    if not ret:break
    frame=cv2.flip(frame,1)
    img = frame.copy()

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)                              
    faces = face_cascade.detectMultiScale(gray)
    totalConf = 0.0
    faceRec = 0
    for (x, y, w, h) in faces:
    	if w+h > boxlimit:
    		cv2.rectangle(frame,(x,y),(w+x,y+h),(0,0,255),6)

    		id, conf = rec.predict(gray[y:y+h, x:x+w])    

    		if conf >= 50 and conf <=95:
    			profile = CATEGORY[id-1]
    			if profile not in present_list: present_list.append(profile)
    			cv2.putText(frame, profile,(x+w//2,y),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,255),2,cv2.LINE_AA)


    		else :
    			cv2.putText(frame, 'Unknown',(x+w//2,y),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,25),2,cv2.LINE_AA)        	
        	
    

    cv2.imshow("ss",frame)
    if cv2.waitKey(5) and 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()


print('''today's present are:''')
for x in present_list:
	print("\t",x)


