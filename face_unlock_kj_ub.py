import cv2
import numpy as np
import face_recognition as fr
from time import time
import os


face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
real_img_path = 'mypic.png'
unlocked = False
ismatch = False



def real_encoding():
    img = cv2.imread(real_img_path)
    img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    encoding = fr.face_encodings(img)
    return encoding



def recognise_face(test_encoding):
    #print(np.array(real_encode).shape,np.array(test_encoding).shape)
    distance = fr.face_distance([real_encode[0]],test_encoding)
    #print(distance)
    if distance < 0.5:
        return True
    else:
        return False

real_encode = real_encoding()

def get_face_image(faces,img):
    detected_faces = []
    for (x,y,w,h) in faces:
        detected_faces.append(img[y:y+h,x:x+w])
    return detected_faces

def face_detect(img):
    global unlocked
    global ismatch
    img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    co_faces = face_detector.detectMultiScale(img,1.3,5)
    faces = get_face_image(co_faces,img)
    if co_faces is not ():
        if not unlocked:
            for f in faces:
                test_encoding = fr.face_encodings(f)
                if test_encoding != []:
                    ismatch = recognise_face(test_encoding[0])
                    if ismatch:
                        break

    if ismatch:
        unlocked = True
        return True



def capture_camera(camera_no):
    cap = cv2.VideoCapture(camera_no)
    res = False
    t1 = time()
    while True:
        check,frame = cap.read()
        res = face_detect(frame)
        t2 = time()
        if t2-t1 > 50 or res:
            return res
    cap.release()
    cv2.destroyAllWindows()
    

res = capture_camera(0)
print(res)

if res:
    os.system('gnome-screensaver-command -d')   

