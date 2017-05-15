import cv2
import glob
import random
import numpy as np
import matplotlib.pyplot as plt

cap = cv2.VideoCapture(0)  # open camera
pic_num = 1

faceDet = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

emotions = ["anger", "happy", "sadness"]  # Emotion list
# Initialize fisher face classifier
fishface = cv2.createFisherFaceRecognizer()


def load_model(i):
    fishface.load(
        'trained_classifiers_new/trained_faceclassifier'+str(i)+'.xml')

for i in range(0, 10):
    load_model(i)
    print "model loaded!"
    pic_num = 1
    for j in range(0, 100):  # capture 100 frames
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        print j
        # Detect face
        face = faceDet.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=10,
                                        minSize=(5, 5),
                                        flags=cv2.CASCADE_SCALE_IMAGE)
        print "here2"
        # Cut and save face
        for (x, y, w, h) in face:  # get coordinates and size of rectangle
            print "face found"
            gray = gray[y:y+h, x:x+w]  # Cut the frame to size
            try:
                out = cv2.resize(gray, (350, 350))
                pred, conf = fishface.predict(out)
                print emotions[pred]
                cv2.imwrite('Demo/'+str(i)+'_'+str(pic_num) +
                            '_'+str(emotions[pred])+'.jpg', out)
                pic_num += 1
            except:
                pass

            # raw_input()

cap.release()
