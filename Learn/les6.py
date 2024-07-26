import numpy as np
import cv2
img = cv2.imread("images/earth.jpg")
new_image = cv2.resize(img, (500 , 300))
cv2.rectangle(new_image,(160,50),(340,250,),(0,255.0),4)   #line - rectangle - text
cv2.putText(new_image,"earth",(160,46),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0),1)
cv2.imshow('show',new_image)
cv2.waitKey(0)


