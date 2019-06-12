import time
import numpy as np
import cv2
from collections import defaultdict
import destination
import path
#import direction
import matrix
x1=int(input("Enter starting point: "))
y1=int(input("Enter the y coordinate: "))
#dir=input("Enter direction: ")
flag=1
sh=input("Enter shape: ")
co=input("Enter color: ")
s=(x1,y1)
a= (matrix.mat())
print (a)
if (x1==4 and y1==0):
    dir='u'
    a[3][4][0:2]=a[4][5][0:2]=a[5][4][0:2]=[0,0]
elif (x1==0 and y1==4):
    dir='r'
    a[4][3][0:2]=a[4][5][0:2]=a[5][4][0:2]=[0,0]
elif (x1==4 and y1==8):
    dir='d'
    a[3][4][0:2]=a[4][3][0:2]=a[5][4][0:2]=[0,0]
elif (x1==8 and y1==4):
    dir='l'
    a[3][4][0:2]=a[4][5][0:2]=a[4][3][0:2]=[0,0]
while (True):
    points=[]
    # d= tuple((destination.dest(a,s,sh,co))[0:2])
    # print (d)
    try:
        d= tuple((destination.dest(a,s,sh,co))[0:2])
        points= (path.paths(s,d))
    except (UnboundLocalError):
        file=open('string.txt','w+')
        file.write('0')
        file.close()
        sh=input("Enter shape: ")
        co=input("Enter color: ")
        continue
    except (RecursionError):
        file=open('string.txt','w+')
        file.write('0')
        file.close()
        sh=input("Enter shape: ")
        co=input("Enter color: ")
        continue
    for i in points:
         i=list(i)
    print (points)
    def direction(x,y):
        #print (x,y)
        if ((x==-1) & (y==0)):
            return 'u'
        elif((x==1) & (y==0)):
            return 'd'
        elif((x==0) & (y==1)):
            return 'r'
        elif((x==0) & (y==-1)):
            return 'l'
    def string(dir,x,y):
        if(((dir=='u') & (x==0) & (y==1))  |  ((dir=='r') & (x==1) & (y==0)) | ((dir=='d') & (x==0) & (y==-1)) | ((dir=='l') & (x==-1) & (y==0))):  # Condition for right direction
            # error()
            return('r')
            # file=open('string.txt','a')
            # file.write(path)
            # file.close()
        elif(((dir=='u') & (x==0) & (y==-1)) | ((dir=='r') & (x==-1) & (y==0)) | ((dir=='d') & (x==0) & (y==1)) | ((dir=='l') & (x==1) & (y==0)) | (dir=='u' and x==1 and y==0)):  # Condition for left direction
            #error()
            return('l')
            # file=open('string.txt','a')
            # file.write(path)
            # file.close()
        elif(((dir=='u') & (x==-1) & (y==0)) | ((dir=='r') & (x==0) & (y==1)) | ((dir=='d') & (x==1) & (y==0)) | ((dir=='l') & (x==0) & (y==-1))):  # Condition for forward direction
            return('f')
            # file=open('string.txt','a')
            # file.write(path)
            # file.close()
    # file=open('string.txt','w+')
    # file.write('')
    # file.close()
    #points=[[0,3],[0,4],[1,4],[2,4],[2,5],[2,6],[3,6],[4,6],[4,7]]

    source=points[0]
    pa=""
    for i in range(len(points)-1): #points is the list of points of the path to be traversed
        # a=points[i][0]
        # b=points[i][1]
        # x=points[i][0]-source[0]
        # y=points[i][1]-source[1]
        # print (y)
        #print (dir)
        # a=points[i+1][0]
        # b=points[i+1][1]
        #print ((list(points[i])))
        x=points[i+1][0]-points[i][0]
        y=points[i+1][1]-points[i][1]
        #print (dir)
        #print (x,y)
        #print (string(dir,x,y))
        pa=string(dir,x,y)
        if(pa=='f'):
            variabletime=4
        elif((pa=='r')|(pa=='l')):
            variabletime=4
        #print (path)
        dir=direction(x,y)
        #print (dir)
        # source=points[i]
        #print (pa)
        file=open('html/string.txt','w+')
        file.write(pa)
        file.close()
        if ((d==(3,4)) | (d==(4,3)) | (d==(5,4)) | (d==(4,5))):
            file=open('html/string.txt','a')
            file.write('fz')
            file.close()
        file=open('html/string.txt','a')
        file.write('0')
        file.close()
        time.sleep(variabletime)
        file=open('html/string.txt','w+')
        file.write("")
        file.close()
        time.sleep(variabletime)
    file=open('html/string.txt','w+')
    file.write("a0")
    file.close()
    sh=input("Enter shape: ")
    co=input("Enter color: ")
    s=tuple(points[-1])
    if (x1==4 and y1==0 and s[0]>4):
        i=0
        while (i<4):
            for j in range(9):
                a[i][j][0:2]=[0,0]
            i=i+1
    if (x1==0 and y1==4 and s[1]<4):
        j=0
        while (j<4):
            for i in range(9):
                a[j][i][0:2]=[0,0]
            j=j+1
    if (x1==4 and y1==8 and s[0]<4):
        i=5
        while (i<9):
            for j in range(9):
                a[i][j][0:2]=[0,0]
            i=i+1
    if (x1==8 and y1==4 and s[1]>4):
        i=5
        while (i<9):
            for j in range(9):
                a[j][i][0:2]=[0,0]
            i=i+1
