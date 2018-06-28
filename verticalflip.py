import os
#read pic
import numpy as np
import cv2
def profile_walk(path):
    return(os.listdir(path))

def detail(path1,path2):
    # Load an color image in color scale
    list1= profile_walk(path1)
    for i in list1:
        if i.split(".")[1]=="jpg"or"JPG"or"png":
            img = cv2.imread(path1 +"/"+i,1)
            print(path1+"/" +i)
            #Flip Vertically
            himg = img.copy()
            himg =cv2.flip(img,0)
            cv2.imwrite(path2+"/"+i,himg)

if __name__ == "__main__":
    path1 = input("输入图片载入路径：")
    path2 = input("输入图片输出路径：")
    detail(path1,path2)
