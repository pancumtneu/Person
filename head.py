import cv2
import os
import showpic
import recong
import smile
import upperbody
import lowerbody
import time
# pathofeye = 'D:\opencv\opencv-master\data\haarcascades\haarcascade_eye.xml'
# pathoffront = 'D:\opencv\opencv-master\data\haarcascades\haarcascade_frontalface_default.xml'

'''
这里注意一定要用全路径   否则报错  error: (-215) !empty() in function cv::CascadeClassifier::detectMultiScale
具体参照   https://blog.csdn.net/qq_20156437/article/details/80702022
我从网上下载了cv2  (https://github.com/opencv/opencv)  这里面包含了分类器模型haarcascade_eye.xml等 我保存的位置是
/home/apollo/pan/cv2/data/haarcascades/ 一定要能寻找到分类器模型

'''

# faceCascade = cv2.CascadeClassifier(pathoffront)
#
#
# rootdir = 'girls'
# list = os.listdir(rootdir) #列出文件夹下所有的目录与文件
# for i in range(0,len(list)):
#        path = os.path.join(rootdir,list[i])
#        if os.path.isfile(path):
#            image = cv2.imread(path)
#
#            size = image.shape
#            h, w = size[0], size[1]  # 获取图片的大小   后续我根据这个比例缩放
#
#            print(h, w)  # 打印大小
#
#            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#            faces = faceCascade.detectMultiScale(gray, scaleFactor=1.2,
#                                                 minNeighbors=5, minSize=(30, 30), )
#            for (x, y, width, height) in faces:
#                cv2.rectangle(image, (x, y), (x + width, y + height), (0, 255, 0), 2)
#                im2 = cv2.resize(image, (int(w * 0.55), int(h * 0.55)), interpolation=cv2.INTER_CUBIC)
#                # int(w*0.55), int(h*0.55)是按照55%的比例缩放，注意这个参数只接受整数，这里需要转换一下
#
#
#                #cv2.imshow(r'liu %s.jpg '%i, im2)
#
#                cv2.imwrite(r'.\header\刘洋 %s.jpg '%i, im2)                #路径拼接方法

smile.detect('girls')
recong.detect('girls')
upperbody.detect("girls")
lowerbody.detect('girls')
cv2.waitKey(0)
# directory ='girls'
#showpic.mypath(directory)             ##显示所有文件
                                    ##image = cv2.imread(r"ly.jpg")  # 读取图片   这里可以加一个判断，否则没有读取到图片还会引起其他莫名其妙的错误

