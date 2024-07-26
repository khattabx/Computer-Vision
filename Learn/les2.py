# عرض الصور مع بقاء النافذه 
import cv2
img = cv2.imread("images/car.jpg")
cv2.imshow("Show", img)
cv2.waitKey(0)  # 0--> for photos , 1--> for videos
