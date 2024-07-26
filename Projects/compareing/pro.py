import cv2
PH1 = cv2.imread('computer_vision/Projects/compareing/w.png')
PH2 = cv2.imread('computer_vision/Projects/compareing/b/R.png')

if PH1.shape == PH2.shape:
    print("the image have the same shape")
    diff = cv2.subtract(PH1, PH2)
    b,g,r = cv2.split(diff)
    if cv2.countNonZero(b) ==0 and cv2.countNonZero(g) and cv2.countNonZero(r):
        print('the images are completely Equal')
else:
    print('the images are not completely Equal')
