import os
import os.path
rootdir = "C:/Users/SEELE/Desktop/bg.1"

file_object = open('C:/Users/SEELE/Desktop/bg,1.txt','w')

for parent,dirnames,filenames in os.walk(rootdir):
    for filename in filenames:
        print (filename)
        file_object.write('bg.1/' + filename + '\n')
file_object.close()
