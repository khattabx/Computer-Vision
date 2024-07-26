# import cv2
# camera = cv2.VideoCapture(0)
# while True:
#     ret , video = camera.read()
#     cv2.imshow("show",video)
#     if cv2.waitKey(1) & 0xff == ord("q"):
#         break


import cv2

camera = cv2.VideoCapture(0)

while True:
    ret, video = camera.read()
    video = cv2.flip(video, 1)  # عكس حركة الكاميرا أفقيا
    cv2.imshow("show", video)
    if cv2.waitKey(1) & 0xff == ord("q"):
        break
