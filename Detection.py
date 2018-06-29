# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 22:56:16 2018

@author: sczjwjh
"""

import cv2

def locations(img):
#    haar = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    haar = cv2.CascadeClassifier('cascade7.xml')
#    image_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#    image_gray = cv2.equalizeHist(image_gray)
    cars = haar.detectMultiScale(img,1.11,5)
    print(len(cars))
    for f_x, f_y, f_w, f_h in cars:
#          Draw a box around the face
        cv2.rectangle(img, (f_x - 10, f_y - 10), (f_x+f_w + 35, f_y+f_h+35), (0, 0, 255), 2)
    return img
#    cv2.namedWindow("test",0);
#    cv2.resizeWindow("test")
if __name__ == "__main__":
    
    
# img
    i =1567
#    while i < 1505:
#    path  = "data/"+str(i)+".jpg"
    path  = "123.jpg"

    image = cv2.imread(path)
    img = locations(image)
    cv2.namedWindow("test"+str(i),0);

    cv2.imshow('test'+str(i),img)
#        i = i + 1
#        cv2.waitKey(0)
#        cv2.destroyWindows('test')
    
# video
#    fourcc = cv2.VideoWriter_fourcc(*'XVID')
#    output_movie = cv2.VideoWriter('output.avi', fourcc, 25.97, (640, 360))
#    input_movie = cv2.VideoCapture("video_3.mp4")
#    frame_number = 0
#    while True:
#    # Grab a single frame of video
#        ret, frame = input_movie.read()
#        frame_number += 1
#
#    # Quit when the input video file ends
#        if not ret:
#            break
#
#    # Write the resulting image to the output video file
#        out_frame = locations(frame)
##        cv2.imshow("test", out_frame)
##        print("Writing frame {} / {}".format(frame_number, length))
##        output_movie.write(out_frame)
#        cv2.imwrite(str(frame_number)+'.jpg',out_frame)
#
## All done!
#    input_movie.release()
    cv2.waitKey(0)
    cv2.destroyAllWindows()

