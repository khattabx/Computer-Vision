# نظام الالوان في الصور
import cv2
img = cv2.imread("images/earth.jpg")
new_image = cv2.resize(img, (500 , 300))
gray = cv2.cvtColor(new_image, cv2.COLOR_BGR2GRAY)
cv2.imshow('show',gray)
cv2.waitKey(0)

