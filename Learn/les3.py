# عرض ابعاد الصوره و البكسلات
import cv2
img = cv2.imread("images/earth.jpg")
cv2.imshow('show', img)
pixels = img.size
dimesions = img.shape
print("number of pixels :", pixels)
print("dimesions :", dimesions )
cv2.waitKey(0)
