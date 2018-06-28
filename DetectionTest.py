# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 22:56:16 2018

@author: sczjwjh
"""

import cv2

def locations(img):
    haar = cv2.CascadeClassifier('cascade6.xml')
    cars = haar.detectMultiScale(img,1.11,5)
    print(len(cars))
    for f_x, f_y, f_w, f_h in cars:
#          Draw a box around the face
        cv2.rectangle(img, (f_x - 10, f_y - 10), (f_x+f_w + 35, f_y+f_h+35), (0, 0, 255), 2)
    return img

if __name__ == "__main__":
    
    
# img
    i =1567
#    while i < 1505:
#    path  = "data/"+str(i)+".jpg"
    path  = "7021.jpg"

    image = cv2.imread(path)
    img = locations(image)
    cv2.namedWindow("test"+str(i),0);

    cv2.imshow('test'+str(i),img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

