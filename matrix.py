import cv2
import numpy as np
#reading the image
'''image = cv2.imread("Pixelate_Track.png",1)
# convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# threshold to get just the signature (INVERTED)
retval, thresh_gray = cv2.threshold(gray, thresh=100, maxval=255, \
                                   type=cv2.THRESH_BINARY_INV)

contours, hierarchy = cv2.findContours(thresh_gray,cv2.RETR_LIST, \
                                   cv2.CHAIN_APPROX_SIMPLE)

# Find object with the biggest bounding box
mx = (0,0,0,0)      # biggest bounding box so far
mx_area = 0
for cont in contours:
    x,y,w,h = cv2.boundingRect(cont)
    area = w*h
    if area > mx_area:
        mx = x,y,w,h
        mx_area = area
x,y,w,h = mx

# Output to files
roi=image[y:y+h,x:x+w]
cv2.imwrite('Image_crop.jpg', roi)
img = cv2.imread('Image_crop.jpg',1)
re = cv2.resize(img  , (900 , 900))
w=9
h=9
m=[[0 for i in range(w)] for j in range(h)]
x=0
y=0
h=100
k=100
i=0
j=0
idx=0
while(i<9):
  if(i < 9) :
    if(j < 9):
      m[0][0]=re[x:x+h,y:y+h]
      y=y+h
      cv2.waitKey(1000)
      j=j+1
      idx+=1
      m[0][0]=m[0][0][5:95,5:95]
      cv2.imshow("input",m[0][0])
      cv2.imwrite(str(idx) + '.png', m[0][0])
      continue
    j =0
    x=x+h
    y=0
    i=i+1
    cv2.waitKey(0)
    continue'''
'''for no in range (1,82):
    img = cv2.imread(str(no) + ".png")
    a =np.zeros((90,90,3), np.uint8)
    a[:] = (255,255,255)
    #cv2.namedWindow('fr1',cv2.WINDOW_NORMAL)
    #cv2.imshow('fr1',img)
    k=0

    for i in range(90):
        for j in range(90):
            if( 15<img[i][j][0] < 60 and img[i][j][1] > 195 and img[i][j][2] > 195):
                a[i][j] = img[i][j]
                k=1
            elif(15<img[i][j][0] < 60 and 15<img[i][j][1] < 60 and img[i][j][2] > 195):
                a[i][j] = img[i][j]
                k=1
            elif( img[i][j][0] < 15 and img[i][j][1] < 15 and img[i][j][2] < 15):
                a[i][j] = img[i][j]
    if k==1:
        cv2.imwrite("bhai"+str(no) + ".png",a)'''
def mat():
    def color_detection(im):
        color="C"
        count=0
        hsv = cv2.cvtColor(im, cv2.COLOR_BGR2HSV)
        mask1 = cv2.inRange(hsv,(12, 210, 241), (31, 255, 255)) #yellow
        mask2 = cv2.inRange(hsv,(0,220,195),(5,255,255))      #red
        A=cv2.moments(mask1)
        B=cv2.moments(mask2)
        try:
            dx= int(A['m10']/A['m00'])
            dy = int(A['m01']/A['m00'])
        except ZeroDivisionError:
            color="R"
            count=1
        try:
            cx= int(B['m10']/B['m00'])
            cy = int(B['m01']/B['m00'])
        except ZeroDivisionError:
            color="Y"
            count=count+1
        if (color=="R" and count!=2):
            return "red"
        elif (color=="Y" and count!=2):
            return "yellow"
        else:
            pass
    def shape(im):
        image = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        if color_detection(im)=="yellow":
            for i in range (90):
                for j in range(90):
                    if (image[i,j]>100 and image[i,j]<250):
                        image[i,j]=255
                    else:
                        image[i,j]=0


        else:
            for i in range (90):
                for j in range(90):
                    if (image[i,j]>0 and image[i,j]<255):
                        image[i,j]=255
                    else:
                        image[i,j]=0

        #finding_contours
        (cnts, _) = cv2.findContours(image.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cv2.drawContours(im,cnts, -1, (0, 255, 0), 2)
        c=cnts[0]
        area = cv2.contourArea(c)
        if 0<=area <= 1450 :
            return("triangle")
        elif 1450<area<= 2000:
            return("circle")
        elif 2000<area<= 5000:
            return("square")
        else:
            return("arrow")
    def centroids(im):
        image = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        if color_detection(im)=="yellow":
            for i in range (90):
                for j in range(90):
                    if (image[i,j]>100 and image[i,j]<250):
                        image[i,j]=255
                    else:
                        image[i,j]=0

        else:
            for i in range (90):
                for j in range(90):
                    if (image[i,j]>0 and image[i,j]<255):
                        image[i,j]=255
                    else:
                        image[i,j]=0
        #finding_contours
        (cnts, _) = cv2.findContours(image.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cv2.drawContours(im,cnts, -1, (0, 255, 0), 2)
        c=cnts[0]
        M = cv2.moments(c)
        cx = int(M['m10']/M['m00'])
        cy = int(M['m01']/M['m00'])
        return [cx,cy]
    im = cv2.imread("images/b1.png")
    a=[[0 for x in range(9)] for y in range(9)]
    k=l=0
    for no in range (1,82):
        im = cv2.imread("images/b"+str(no)+".png")
        try:
            c=color_detection(im)
            s=shape(im)
            m=centroids(im)
            if (s=='arrow'):
                c=0
                s=1
            elif (c==None):
                c=0
                s=0
        except IndexError:
            while (k<9):
                while(l<9):
                    a[k][l]=[0,0,k,l,m]
                    l=l+1
                    break
                if (l==9):
                    k=k+1
                    l=0
                break
        else:
            while (k<9):
                while(l<9):
                    a[k][l]=[s,c,k,l,m]
                    l=l+1
                    break
                if (l==9):
                    k=k+1
                    l=0
                break

    return (a)
