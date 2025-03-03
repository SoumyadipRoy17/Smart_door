# import pickle,time
# import cv2
# import pyttsx3   #offline lib for tts
# import serial  #for serial communication with arduino
#
#
# #Establish connection with arduino
# # arduino = serial.Serial(port='COM3', baudrate=9600, timeout=.1)
#
# #Specify the recognizer
# face_cascade=cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_alt2.xml')
# recognizer = cv2.face.LBPHFaceRecognizer_create()
# recognizer.read('trainer.yml')  # Reading the stored trained model.
#
# #Initiallize speech engine
# engine = pyttsx3.init()
#
# #Loading the label-id relation to get the name of the labels.
# with open("label_ids.pickle",'rb') as fr:
#     og_labels=pickle.load(fr)
#
# #labels are of the form {name:id} we want to invert this form to {id:name}
# labels={k:v for v,k in og_labels.items()}
#
#
# print(labels)
# # face_cascade=cv2.CascadeClassifier('haarcascade_profileface.xml')
#
# def speak(text):  #fn to convert text to speech
#     engine.say(text)
#     engine.runAndWait()
#
# def face_recognition():
#     flag_face_recognised=False   #to keep track if the user face is recognized
#     flag_face_not_recognised=False
#
#     no_of_adjacent_prediction=0
#     no_face_detected=0  #to track the number of times the face is detected
#     prev_predicted_name=''   #to keep track of the previously predicted face(w.r.t frame)
#     cap=cv2.VideoCapture(0)
#     count_frames = total_no_face_detected = 0
#
#
#
#
#
#     while True:
#         count_frames+=1
#         ret,frame = cap.read()
#         # print(ret,frame)
#         gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#
#         faces=face_cascade.detectMultiScale(gray,scaleFactor=1.2,minNeighbors=5)
#
#         # print("FACES : ",faces)
#         # print(type(frame))   #The frames are automatically converted into numpy arrays of pixels.
#         for (x,y,w,h) in faces:
#
#             total_no_face_detected+=1
#             no_face_detected+=1
#
#             # print(x,y,w,h)
#             roi_gray=gray[y:y+h,x:x+w]  #roi(region of interest)
#             # roi_color=frame[y:y+h,x:x+w]
#             id,confidence=recognizer.predict(roi_gray)
#             print(id,confidence)
#             if(confidence>70):
#                 print("PREDICTED : ",labels[id])
#                 font=cv2.FONT_HERSHEY_SIMPLEX
#                 name=labels[id]
#                 clr=(255,255,255);thickness=2
#                 cv2.putText(frame,name.replace('_',' ').title(),(x,y-5),font,0.8,clr,1,cv2.LINE_AA)
#
#
#                 if(prev_predicted_name==name):
#                     no_of_adjacent_prediction+=1
#                 else:
#                     no_of_adjacent_prediction=0
#
#                 prev_predicted_name=name
#
#
#
#             # color=(255,0,0) #BGR 0-255
#             thickness=1
#             end_coord_x=x+w
#             end_coord_y=y+h
#
#
#             if(no_of_adjacent_prediction>15):   #no_of_adjacent_prediction is only updated when the confidence of classification is >80
#                 cv2.putText(frame,"Welcome home "+name.replace('_',' ').title(),(160,460),font,0.8,clr,thickness,cv2.LINE_AA)  #to print on frame
#                 flag_face_recognised=True
#                 no_of_adjacent_prediction=0
#                 no_face_detected=0
#
#             elif(no_face_detected>=30):
#                 cv2.putText(frame,"Face Not Recognised",(160,460),font,0.8,clr,thickness,cv2.LINE_AA)
#                 flag_face_not_recognised=True
#                 no_of_adjacent_prediction=0
#                 no_face_detected=0
#
#             cv2.rectangle(frame,(x,y),(end_coord_x,end_coord_y),(0,0,0),2)  #Drawing the rectangle on the frame
#
#         cv2.imshow('Face Recognition',frame)
#
#         if(flag_face_recognised):    #if face is recognized then open the door
#             speak("Welcome "+name.replace('_',' ')+", unlocking door. The door will remain open for the next 5 seconds")
#             print("DOOR is OPEN")
#             #arduino.write(bytes('o', 'utf-8'))  #Output the given byte string over the serial port.
#
#             time.sleep(5)
#             speak("Closing door")
#             #arduino.write(bytes('c', 'utf-8'))  #Output the given byte string over the serial port.
#             print("DOOR is CLOSED")
#             flag_face_recognised=False
#             return True
#
#         if(flag_face_not_recognised):
#             speak("Face not recognised. The door will remain closed")
#             time.sleep(2)
#             flag_face_not_recognised=False
#             return False
#
#
#         k=cv2.waitKey(20)     #the key is recieved and converted into ascii value
#         if k==113:  #compairing with the ordinal/ascii value of 'q'
#             break
#
#
#     print("No. of frames : ",count_frames," |   No. of times face detected : ",total_no_face_detected)
#     cap.release()
#     cv2.destroyAllWindows()
#
#
#
#
# if(__name__=="__main__"):
#     face_recognition()
# #
# # import pickle
# # import time
# # import cv2
# # import pyttsx3  # Offline library for TTS
# #
# # # Specify the recognizer
# # face_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_alt2.xml')
# # recognizer = cv2.face.LBPHFaceRecognizer_create()
# # recognizer.read('trainer.yml')  # Reading the stored trained model.
# #
# # # Initialize speech engine
# # engine = pyttsx3.init()
# #
# # # Loading the label-id relation to get the name of the labels.
# # with open("label_ids.pickle", 'rb') as fr:
# #     og_labels = pickle.load(fr)
# #
# # # Inverting labels to {id: name}
# # labels = {v: k for k, v in og_labels.items()}
# #
# # def speak(text):
# #     engine.say(text)
# #     engine.runAndWait()
# #
# # def face_recognition():
# #     no_of_adjacent_prediction = 0
# #     no_face_detected = 0
# #     prev_predicted_name = ''
# #     cap = cv2.VideoCapture(0)
# #     count_frames = total_no_face_detected = 0
# #
# #     while True:
# #         count_frames += 1
# #         ret, frame = cap.read()
# #         if not ret:
# #             print("[ERROR] Camera not detected!")
# #             break
# #
# #         gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
# #         faces = face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5)
# #
# #         for (x, y, w, h) in faces:
# #             total_no_face_detected += 1
# #             no_face_detected += 1
# #             roi_gray = gray[y:y + h, x:x + w]
# #             id, confidence = recognizer.predict(roi_gray)
# #
# #             if confidence > 70:
# #                 name = labels[id]
# #                 if prev_predicted_name == name:
# #                     no_of_adjacent_prediction += 1
# #                 else:
# #                     no_of_adjacent_prediction = 0
# #                 prev_predicted_name = name
# #
# #                 if no_of_adjacent_prediction > 15:
# #                     speak(f"Welcome {name.replace('_', ' ')}, unlocking door.")
# #                     print("[SUCCESS] Face Recognized! Unlocking door...")
# #                     cap.release()
# #                     cv2.destroyAllWindows()
# #                     return True
# #
# #             if no_face_detected >= 30:
# #                 speak("Face not recognised. The door will remain closed.")
# #                 print("[ERROR] Face Not Recognized!")
# #                 cap.release()
# #                 cv2.destroyAllWindows()
# #                 return False
# #
# #         cv2.imshow('Face Recognition', frame)
# #         if cv2.waitKey(20) & 0xFF == ord('q'):
# #             break
# #
# #     cap.release()
# #     cv2.destroyAllWindows()
# #     return False

import cv2
import dlib
import yaml
import numpy as np

# Load Dlib models
detector = dlib.get_frontal_face_detector()
sp = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
facerec = dlib.face_recognition_model_v1("dlib_face_recognition_resnet_model_v1.dat")

# Load trained embeddings
with open("trainer.yml", "r") as f:
    train_data = yaml.safe_load(f)

label_id = train_data["labels"]
stored_embeddings = np.array(train_data["embeddings"])
label_ids = np.array(train_data["label_ids"])

# Reverse the label_id dictionary for name lookup
id_to_label = {v: k for k, v in label_id.items()}


# Function to find the best match for a detected face
def recognize_face(face_descriptor):
    distances = np.linalg.norm(stored_embeddings - face_descriptor, axis=1)
    min_distance = np.min(distances)

    if min_distance < 0.6:  # Adjust threshold as needed
        best_match_index = np.argmin(distances)
        return id_to_label[label_ids[best_match_index]]
    else:
        return "Unknown"


# Open webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Convert frame to grayscale for detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Detect faces
    faces = detector(gray)

    for d in faces:
        shape = sp(gray, d)
        face_descriptor = np.array(facerec.compute_face_descriptor(gray, shape))

        name = recognize_face(face_descriptor)

        # Draw rectangle and label
        x, y, w, h = d.left(), d.top(), d.width(), d.height()
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(frame, name, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

    # Show frame
    cv2.imshow("Face Recognition", frame)

    # Exit on pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
