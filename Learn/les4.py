# تغير حجم الصوره  والنافذه
import cv2
img = cv2.imread("images/earth.jpg")
new_image = cv2.resize(img, (1000 , 800))
cv2.imshow('show',new_image)
cv2.waitKey(0)
