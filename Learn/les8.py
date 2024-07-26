# عرض الفيديوهات في البرنامج
import cv2 
cam = cv2.VideoCapture('video/DrStrange.mp4')
while True :
    ret , frame = cam.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # color
    size = cv2.resize(frame, (800,450))
    cv2.imshow("Dr Strange",size)
    if cv2.waitKey(1) & 0xff == ord("q"):
        break


