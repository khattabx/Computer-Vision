import cv2
MODEL_MEAN_VALUES = (78.4463377603, 87.7689143744, 114.895847746)
ageList = ["(0-2)", "(4-6)", "(8-12)", "(15-20)", "(25-32)", "(38-43)", "(48-53)", "(60-100)"]
genderList = ["Male", "Female"]

def filesGet():
    age_net = cv2.dnn.readNetFromCaffe('computer_vision/Projects/Age_Expectancy/data/deploy_age.prototxt' , 'computer_vision/Projects/Age_Expectancy/data/age_net.caffemodel')
    gender_net = cv2.dnn.readNetFromCaffe('computer_vision/Projects/Age_Expectancy/data/deploy_gender.prototxt' , 'computer_vision/Projects/Age_Expectancy/data/gender_net.caffemodel')
    return age_net, gender_net

def read_from_camera(age_net, gender_net):
    image = cv2.imread('computer_vision/Projects/Age_Expectancy/images/test1.jpg')      # put your photo here
    face_cascade = cv2.CascadeClassifier('computer_vision/Projects/Age_Expectancy/data/haarcascade_frontalface_alt.xml')
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 5)

    if len(faces) > 0:
        print("Found {} Faces".format(len(faces)))


    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 255, 0), 2)
        face_img = image[y:y+h, x:x+w].copy()
        blob = cv2.dnn.blobFromImage(face_img, 1, (227, 227), MODEL_MEAN_VALUES, swapRB=False)
        gender_net.setInput(blob)
        gender_p = gender_net.forward()
        gender = genderList[gender_p[0].argmax()] 
        age_net.setInput(blob)
        age_p = age_net.forward()
        age = ageList[age_p[0].argmax()]
        G_A = "%s %s" % (gender, age)
        font = cv2.FONT_HERSHEY_PLAIN
        cv2.putText(image, G_A, (x, y), font, 1, (0, 255 , 0), 1, cv2.LINE_AA)
        cv2.imshow('gender & age expectancy', image)
        cv2.waitKey(0)

if __name__ == "__main__":
    age_net, gender_net = filesGet()
    read_from_camera(age_net, gender_net)

