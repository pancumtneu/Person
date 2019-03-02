#!/usr/bin/python
# -*- coding: UTF-8 -*-
import cv2
import os
os.mkdir('headerss')
# cv2.waitKey(0)


rootdir = 'girls'
list = os.listdir(rootdir) #列出文件夹下所有的目录与文件

for i in range(0,len(list)):
       path = os.path.join(rootdir,list[i])
       if os.path.isfile(path):
           img = cv2.imread(path)

           # font = cv2.FONT_HERSHEY_SIMPLEX
           #font = cv2.FONT_HERSHEY_DUPLEX
           font=cv2.FONT_HERSHEY_TRIPLEX
           imgzi = cv2.putText(img, 'love you ', (100, 100), font, 2.2, (128, 10, 255), 4)
           cv2.imshow("pic,jpg", imgzi)

           cv2.imwrite(r'.\headerss\ 刘洋 %s.jpg '%i, imgzi)              #路径拼接方法
cv2.waitKey(0)