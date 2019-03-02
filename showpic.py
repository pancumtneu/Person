import cv2
import os
directory ='girls'
def mypath(dirs):

    list = os.listdir(dirs)  # 列出文件夹下所有的目录与文件

    for i in range(0, len(list)):
        path = os.path.join(dirs, list[i])
        if os.path.isfile(path):
            print(path)
            # cv2.imshow(r'girls\1b1b521ba28b4c21a4b050648fc5958c_th.jpg')
            img=cv2.imread(path)
            cv2.imshow(r'liu%s.jpg ' % i, img)



#
# if __name__=='__main__':  # 调用显示函数的方法
#     mypath(directory)
#     cv2.waitKey(0)