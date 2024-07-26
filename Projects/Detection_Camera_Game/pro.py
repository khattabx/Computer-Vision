import math
import random
import cv2
import cvzone
from cvzone.HandTrackingModule import HandDetector

cap = cv2.VideoCapture(0)
cap.set(3,800) # width
cap.set(4,600) # height
detector = HandDetector(detectionCon=0.7, maxHands=1)

class SnakeGame :
     def __init__(self, passFood):
          self.points = [] # to detect all points of the snake
          self.length = [] # to detect the length between a point & another one
          self.currentLength = 0 # the full length of the snake
          self.allowedLength = 150 # maximum length
          self.perviousHead = 0,0 #the last point after the head of the snake
          self.imageFood = cv2.imread(passFood, cv2.IMREAD_UNCHANGED)
          print("Shape of self.imageFood:", self.imageFood.shape)  # Print the shape of the loaded image

          if len(self.imageFood.shape) == 2: # Grayscale image
               self.hFood, self.wfood = self.imageFood.shape
          elif len(self.imageFood.shape) == 3: # Color image
               self.hFood, self.wfood, _ = self.imageFood.shape
          elif len(self.imageFood.shape) == 4: # Image with alpha channel (RGBA)
               self.hFood, self.wfood, _ = self.imageFood.shape[:3]
          else:
               raise ValueError("Unsupported image format")

          self.foodpoints = 0, 0 # Initialize food points
          self.randomFoodLocation()
     def randomFoodLocation(self):
          self.foodpoints = random.randint(100,600), random.randint(100,400)

     def update(self, frameMain, currentHead ):
          px , py = self.perviousHead
          cx , cy = currentHead
          self.points.append([cx, cy])
          distance = math.hypot(cx - px, cy - py)
          self.length.append(distance)
          self.currentLength += distance
          self.perviousHead = cx,cy

          # Reduce the length of the snake
          if self.currentLength > self.allowedLength:
               for i, length in enumerate(self.length):
                    self.currentLength -= length
                    self.length.pop(i)
                    self.points.pop(i)
                    if self.currentLength < self.allowedLength:
                         break

          # foodd eating
          rx, ry = self.foodpoints
          if rx - self.wfood//2 < cx < rx + self.wfood//2 and ry - self.hFood//2 < cy < ry + self.hFood//2:
               self.randomFoodLocation()
               self.allowedLength += 25

          if self.points:
               for i , points in enumerate(self.points):
                    if i != 0 :
                         cv2.line(frameMain,self.points[i-1],self.points[i],(0,0,225),10)
                    cv2.circle(frameMain,self.points[-1],10,(200,0,200),cv2.FILLED)

          # to draw food
               rx , ry = self.foodpoints
               frameMain = cvzone.overlayPNG(frameMain, self.imageFood, (rx-self.wfood//2, ry-self.hFood//2))

          return frameMain

game = SnakeGame('computer_vision/Projects/Detection_Camera_Game/appel/12.png')

while True:
     success , frame = cap.read()
     frame = cv2.flip(frame, 1)
     hands, frame = detector.findHands(frame, flipType = False)

     if hands:
          lmlist = hands[0]['lmList']
          pointIndex = lmlist[8][0:2]
          # cv2.circle(frame,pointIndex,20,(200,0,200),cv2.FILLED)
          frame = game.update(frame,pointIndex)

     key = cv2.waitKey(1)
     cv2.imshow('Snake Game [AI] ', frame)

