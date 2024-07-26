import cv2 
img = cv2.imread("computer_vision/Projects/Image_Explorer/images/employee.png")
classnames = []
classfile = 'computer_vision/Projects/Image_Explorer/files/thing.names'

with open(classfile, 'rt') as f :
    classnames = f.read().rstrip('\n').split('\n')
print(classnames)

p = 'computer_vision/Projects/Image_Explorer/files/frozen_inference_graph.pb'
v = 'computer_vision/Projects/Image_Explorer/files/ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'

net = cv2.dnn_DetectionModel(p,v)
net.setInputSize(320,230)
net.setInputScale(1.0/127.5)
net.setInputMean((127.5,127.5,127.5))
net.setInputSwapRB(True)

classIds, confs, bbox = net.detect(img, confThreshold=0.5)

for classId , confidence , box in zip(classIds.flatten(),confs.flatten(),bbox):
    cv2.rectangle(img,box,color=(0,225,0),thickness=3)
    cv2.putText(img,classnames[classId-1],
                (box[0]+10,box[1]+20),
                cv2.FONT_HERSHEY_DUPLEX,1,(0,0,225),thickness=2)

cv2.imshow("Program",img)
cv2.waitKey(0)




