import cv2
import mediapipe as mp

cap = cv2.VideoCapture(0)
mp_hand = mp.solutions.hands
hands = mp_hand.Hands()
hand_draw = mp.solutions.drawing_utils

while True:
    st, frame = cap.read()
    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb_frame)
    if result.multi_hand_landmarks is not None:
        print(result.multi_hand_landmarks)
        for hand in result.multi_hand_landmarks:
            hand_draw.draw_landmarks(frame, hand, mp_hand.HAND_CONNECTIONS) 

    cv2.imshow('Hand detection', frame)
    if cv2.waitKey(30) & 0xff == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()