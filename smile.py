import cv2
import os

if os.path.isdir('smile'):
    pass
else:
    os.mkdir('smile')
import time
pathofeye = 'D:\opencv\opencv-master\data\haarcascades\haarcascade_eye.xml'
pathoffront = 'D:\opencv\opencv-master\data\haarcascades\haarcascade_smile.xml'
faceCascade = cv2.CascadeClassifier(pathoffront)
#rootdir = 'girls'
def detect(rootdir):


    list = os.listdir(rootdir)               # 列出文件夹下所有的目录与文件
    for i in range(0, len(list)):
        path = os.path.join(rootdir, list[i])
        if os.path.isfile(path):
            image = cv2.imread(path)

            size = image.shape
            h, w = size[0], size[1]  # 获取图片的大小   后续我根据这个比例缩放

            print(h, w)  # 打印大小

            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            faces = faceCascade.detectMultiScale(gray, scaleFactor=1.2,
                                                 minNeighbors=5, minSize=(30, 30), )
            for (x, y, width, height) in faces:
                cv2.rectangle(image, (x, y), (x + width, y + height), (0, 255, 0), 2)
                im2 = cv2.resize(image, (int(w * 0.55), int(h * 0.55)), interpolation=cv2.INTER_CUBIC)
                # int(w*0.55), int(h*0.55)是按照55%的比例缩放，注意这个参数只接受整数，这里需要转换一下

                cv2.imshow(r'liu %s.jpg '% i, im2)
                cv2.imwrite(r'.\smile\ liu %s.jpg ' % i, im2)  # 路径拼接方法



# if __name__=='__main__':  # 调用显示函数的方法
#     detect('girls')
# cv2.waitKey(0)