import cv2
import numpy as np
im=cv2.imread('images/5.png')
image = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
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
print (area)
