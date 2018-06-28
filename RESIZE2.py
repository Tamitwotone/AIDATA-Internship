import numpy as np
import os
import cv2

## 同化图片尺寸
def resize_imgs(imgs, tar_size=None):
    if tar_size:
        resized_imgs =[]
        i=5
        for img in imgs:
            resized = cv2.resize(img, tar_size)
            cv2.imwrite("C:\Users\SEELE\Desktop\cascade Classifier\POSandNEG\POSresize100"+str(i)+ ".jpg",resized)
            resized_imgs.append(resized)
            i+=1
        return np.asarray(resized_imgs)
    else:
        return print('Resize failed, please set a target size...')
## 获取图片数据集
def read_imgs(folder_path):
    files = os.listdir(folder_path)
    imgs = []
    for file in files:
        if file.split(".")[1]=="jpg":
            img = cv2.imread(folder_path + file)
            print(folder_path + file)
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            imgs.append(img)
    return np.asarray(imgs)

POS = read_imgs("C:\Users/SEELE/Desktop/cascade Classifier/POSandNEG/test/")
result = resize_imgs(POS,(100,100))
print(result[0].shape)
