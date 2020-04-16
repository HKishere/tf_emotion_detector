#!/usr/bin/env python
# -*- coding: utf-8 -*-
import cv2
import numpy

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_frontalface_default.xml")
cam = cv2.VideoCapture(0)

model_path = 'my_model_weights.h5'
emotion_label = ['anger', 'disgust', 'Surprised',
                'happy', 'sad', 'afriad', 'natural']

emotion_classifier = load_model(model_path, compile=False)
def EmtionDetect (img):
    face_area = img[y:y+h, x:x+w]
    face_area_gray = cv2.cvtColor(face_area, cv2.COLOR_BGR2GRAY)
    face_area_gray = cv2.resize(face_area_gray,(48, 48))
    emotion_prediction = emotion_classifier.predict(face_area_gray)
    emotionprobability = np.max(emotion_prediction)
    emotion_label_arg = np.argmax(emotion_prediction)
    emotion_text = emotion_labels[emotion_label_arg]

while(True):
    ret, frame = cam.read()
    faces = face_cascade.detectMultiScale(frame, 1.3, 5)
    img = frame
    for (x,y,w,h) in faces:
        img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        EmtionDetect(img)
    cv2.imshow('frame',img)
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

