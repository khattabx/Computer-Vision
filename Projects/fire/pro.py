import cv2
from playsound import playsound # type: ignore
fire_cascade = cv2.CascadeClassifier('Projects/fire/fire_detection.xml')
camera = cv2.VideoCapture(0)
while (True):
    ret, frame = camera.read()
    frame = cv2.flip(frame, 1)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    fire = fire_cascade.detectMultiScale(gray,1.2,5)
    for(x,y,w,h) in fire:
        roi_gray = gray[y:y+h , x:x+w]
        roicolor = frame[y:y+h , x:x+w]
        print('fire is detected')
        playsound('Projects/fire/fire_alarm.mp3')
    cv2.imshow("show", frame)
    if cv2.waitKey(1) & 0xff ==ord('q') :
        break