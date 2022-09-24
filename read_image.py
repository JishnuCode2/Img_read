from socket import RCVALL_SOCKETLEVELONLY
import cv2
import numpy

img = cv2.imread('C:/Users/JISHNU D/Desktop/C116/poster.jpg')

rocket = img[120:360,400:500]
img[0:240,500:600] = rocket

text_2_show = 'I LOVE CODING'
cv2.putText(img,text_2_show,(20,220),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=1,color=(0,0,255))

cv2.imshow('Display Image',img)
print(img)



#gray_img = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
#cv2.imshow('Display Image',gray_img)
cv2.waitKey(0)

