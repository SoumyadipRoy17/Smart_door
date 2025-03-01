# import cv2
# import numpy as np
# from pyzbar.pyzbar import decode  # Pyzbar helps in detection and decoding of the QR code
# from faces import face_recognition
# import time
# import serial  # For Arduino communication
# from secret_key import key, registered_users  # Import key and registered users
#
# # Set up serial communication with Arduino (Change 'COM3' to your correct port)
# try:
#     arduino = serial.Serial(port='COM3', baudrate=9600, timeout=1)  # Adjust COM port for your system
#     time.sleep(2)  # Give time for the connection to establish
# except Exception as e:
#     print(f"[ERROR] Could not connect to Arduino: {e}")
#     arduino = None  # Prevents crashes if Arduino is not connected
#
# cap = cv2.VideoCapture(0)
#
# # Generate the expected QR data format
# valid_qr_data = f"Key: {key}\nRegistered Users: {', '.join(registered_users)}"
#
# # Counter for incorrect attempts
# incorrect_attempts = 0
# max_attempts = 3  # Set a limit for invalid QR scans
#
# while True:
#     success, frame = cap.read()
#
#     if not success:
#         print("[ERROR] Camera not detected!")
#         break
#
#     found_qr = False  # Flag to check if a QR code is detected in the frame
#
#     for i in decode(frame):
#         found_qr = True  # QR code found in the frame
#         decoded_data = i.data.decode("utf-8").strip()  # Converts bytes to string value
#         print(f"[INFO] QR Code detected:\n{decoded_data}")
#
#         # Drawing polygon around the QR code
#         pts = np.array([i.polygon], np.int32)
#         pts = pts.reshape((-1, 1, 2))
#         cv2.polylines(frame, [pts], True, (0, 255, 0), 2)  # Green polygon for detected QR
#
#         # Display decoded text
#         rect_pts = i.rect  # Using rect point for text display
#         font_scale = 0.8
#         thickness = 2
#         cv2.putText(frame, "QR Scanned", (rect_pts[0], rect_pts[1]), cv2.FONT_HERSHEY_SIMPLEX, font_scale, (255, 0, 0),
#                     thickness)
#
#         # Check if QR code is valid
#         if decoded_data == valid_qr_data:
#             print("[SUCCESS] QR Code Valid! Proceeding to face recognition...")
#
#             # Perform face recognition
#             face_recognition()
#
#             # Send a signal to Arduino to unlock using the servo motor
#             if arduino:
#                 print("[INFO] Sending unlock signal to Arduino...")
#                 arduino.write(b'1')  # Sending signal '1' to Arduino to rotate servo
#                 time.sleep(2)  # Allow time for Arduino to process
#
#             cap.release()
#             cv2.destroyAllWindows()
#             exit()
#         else:
#             print(f"[WARNING] Invalid QR Code. Please try again!")
#             incorrect_attempts += 1
#             if incorrect_attempts >= max_attempts:
#                 print("[ERROR] Too many invalid attempts! Exiting system...")
#                 cap.release()
#                 cv2.destroyAllWindows()
#                 exit()
#
#     # If no QR code is found, print a message
#     if not found_qr:
#         print("[INFO] No QR Code detected. Waiting for valid QR...")
#
#     cv2.imshow('QR Authentication', frame)
#
#     # Exit on pressing 'q'
#     ch = cv2.waitKey(1) & 0xFF
#     if ch == ord('q'):
#         print("[INFO] User exited the program.")
#         break
#
# # Cleanup
# cap.release()
# cv2.destroyAllWindows()
#
# # Close Arduino connection
# if arduino:
#     arduino.close()
#
# import cv2
# import numpy as np
# from pyzbar.pyzbar import decode  # Pyzbar helps in detection and decoding of the QR code
# from faces import face_recognition
# import time
# import serial  # For Arduino communication
# from secret_key import key, registered_users  # Import key and registered users
#
# # Set up serial communication with Arduino (Change 'COM3' to your correct port)
# try:
#     arduino = serial.Serial(port='COM3', baudrate=9600, timeout=1)  # Adjust COM port for your system
#     time.sleep(2)  # Give time for the connection to establish
# except Exception as e:
#     print(f"[ERROR] Could not connect to Arduino: {e}")
#     arduino = None  # Prevents crashes if Arduino is not connected
#
# cap = cv2.VideoCapture(0)
#
# # Generate the expected QR data format
# valid_qr_data = f"Key: {key}\nRegistered Users: {', '.join(registered_users)}"
#
# # Counter for incorrect attempts
# incorrect_attempts = 0
# max_attempts = 3  # Set a limit for invalid QR scans
#
# while True:
#     success, frame = cap.read()
#
#     if not success:
#         print("[ERROR] Camera not detected!")
#         break
#
#     found_qr = False  # Flag to check if a QR code is detected in the frame
#
#     for i in decode(frame):
#         found_qr = True  # QR code found in the frame
#         decoded_data = i.data.decode("utf-8").strip()  # Converts bytes to string value
#         print(f"[INFO] QR Code detected:\n{decoded_data}")
#
#         # Drawing polygon around the QR code
#         pts = np.array([i.polygon], np.int32)
#         pts = pts.reshape((-1, 1, 2))
#         cv2.polylines(frame, [pts], True, (0, 255, 0), 2)  # Green polygon for detected QR
#
#         # Display decoded text
#         rect_pts = i.rect  # Using rect point for text display
#         font_scale = 0.8
#         thickness = 2
#         cv2.putText(frame, "QR Scanned", (rect_pts[0], rect_pts[1]), cv2.FONT_HERSHEY_SIMPLEX, font_scale, (255, 0, 0),
#                     thickness)
#
#         # Check if QR code is valid
#         if decoded_data == valid_qr_data:
#             print("[SUCCESS] QR Code Valid! Proceeding to face recognition...")
#
#             # Perform face recognition
#             if face_recognition():
#                 print("[SUCCESS] Face Recognition Successful!")
#
#                 # Send a signal to Arduino to unlock using the servo motor
#                 if arduino:
#                     print("[INFO] Sending unlock signal to Arduino...")
#                     arduino.write(b'o')  # Sending 'o' to Arduino to rotate servo
#                     time.sleep(2)  # Allow time for Arduino to process
#
#                 # Close the system after unlocking
#                 cap.release()
#                 cv2.destroyAllWindows()
#                 exit()
#             else:
#                 print("[ERROR] Face Recognition Failed!")
#
#         else:
#             print(f"[WARNING] Invalid QR Code. Please try again!")
#             incorrect_attempts += 1
#             if incorrect_attempts >= max_attempts:
#                 print("[ERROR] Too many invalid attempts! Exiting system...")
#                 cap.release()
#                 cv2.destroyAllWindows()
#                 exit()
#
#     # If no QR code is found, print a message
#     if not found_qr:
#         print("[INFO] No QR Code detected. Waiting for valid QR...")
#
#     cv2.imshow('QR Authentication', frame)
#
#     # Exit on pressing 'q'
#     ch = cv2.waitKey(1) & 0xFF
#     if ch == ord('q'):
#         print("[INFO] User exited the program.")
#         break
#
# # Cleanup
# cap.release()
# cv2.destroyAllWindows()
#
# # Close Arduino connection
# if arduino:
#     arduino.close()

#
# #working code
# from pymongo import MongoClient
# import datetime
# import cv2
# import numpy as np
# from pyzbar.pyzbar import decode
# from faces import face_recognition
# import time
# import serial
# from secret_key import key, registered_users
# from db import insert_access_log  # Import the function to insert logs
#
# # Set up serial communication with Arduino
# try:
#     arduino = serial.Serial(port='COM3', baudrate=9600, timeout=1)
#     time.sleep(2)
# except Exception as e:
#     print(f"[ERROR] Could not connect to Arduino: {e}")
#     arduino = None
#
# cap = cv2.VideoCapture(0)
# valid_qr_data = f"Key: {key}\nRegistered Users: {', '.join(registered_users)}"
# incorrect_attempts = 0
# max_attempts = 3
#
# while True:
#     success, frame = cap.read()
#     if not success:
#         print("[ERROR] Camera not detected!")
#         break
#
#     found_qr = False
#     for i in decode(frame):
#         found_qr = True
#         decoded_data = i.data.decode("utf-8").strip()
#         print(f"[INFO] QR Code detected:\n{decoded_data}")
#
#         pts = np.array([i.polygon], np.int32)
#         pts = pts.reshape((-1, 1, 2))
#         cv2.polylines(frame, [pts], True, (0, 255, 0), 2)
#         rect_pts = i.rect
#         cv2.putText(frame, "QR Scanned", (rect_pts[0], rect_pts[1]), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2)
#
#         if decoded_data == valid_qr_data:
#             print("[SUCCESS] QR Code Valid! Proceeding to face recognition...")
#             if face_recognition():
#                 print("[SUCCESS] Face Recognition Successful!")
#                 insert_access_log("Success",decoded_data)  # Log access to MongoDB
#
#                 if arduino:
#                     print("[INFO] Sending unlock signal to Arduino...")
#                     arduino.write(b'o')
#                     time.sleep(2)
#
#                 cap.release()
#                 cv2.destroyAllWindows()
#                 exit()
#             else:
#                 print("[ERROR] Face Recognition Failed!")
#                 insert_access_log("Failed")  # Log failed access
#         else:
#             print("[WARNING] Invalid QR Code. Please try again!")
#             incorrect_attempts += 1
#             if incorrect_attempts >= max_attempts:
#                 print("[ERROR] Too many invalid attempts! Exiting system...")
#                 cap.release()
#                 cv2.destroyAllWindows()
#                 exit()
#
#     if not found_qr:
#         print("[INFO] No QR Code detected. Waiting for valid QR...")
#
#     cv2.imshow('QR Authentication', frame)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         print("[INFO] User exited the program.")
#         break
#
# cap.release()
# cv2.destroyAllWindows()
# if arduino:
#     arduino.close()

#
# from pymongo import MongoClient
# import datetime
# import cv2
# import numpy as np
# from pyzbar.pyzbar import decode
# from faces import recognize_face, detector, sp, facerec
# import time
# import serial
# from secret_key import key, registered_users
# from db import insert_access_log
#
# # Set up serial communication with Arduino
# try:
#     arduino = serial.Serial(port='COM3', baudrate=9600, timeout=1)
#     time.sleep(2)
# except Exception as e:
#     print(f"[ERROR] Could not connect to Arduino: {e}")
#     arduino = None
#
# valid_qr_data = f"Key: {key}\nRegistered Users: {', '.join(registered_users)}"
# incorrect_attempts = 0
# max_attempts = 3
#
# cap = cv2.VideoCapture(0)  # Open the camera initially
#
# while True:
#     success, frame = cap.read()
#     if not success:
#         print("[ERROR] Camera not detected!")
#         break
#
#     found_qr = False
#
#     for i in decode(frame):
#         found_qr = True
#         decoded_data = i.data.decode("utf-8").strip()
#         print(f"[INFO] QR Code detected:\n{decoded_data}")
#
#         pts = np.array([i.polygon], np.int32)
#         pts = pts.reshape((-1, 1, 2))
#         cv2.polylines(frame, [pts], True, (0, 255, 0), 2)
#         rect_pts = i.rect
#         cv2.putText(frame, "QR Scanned", (rect_pts[0], rect_pts[1]), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2)
#
#         if decoded_data == valid_qr_data:
#             print("[SUCCESS] QR Code Valid! Proceeding to face recognition...")
#
#             cap.release()  # Close the camera temporarily
#             time.sleep(5)  # Short delay before reopening
#
#             cap = cv2.VideoCapture(0)  # Reopen the camera for face recognition
#
#             while True:
#                 ret, face_frame = cap.read()
#                 if not ret:
#                     print("[ERROR] Camera error while capturing face frame!")
#                     continue
#
#                 gray = cv2.cvtColor(face_frame, cv2.COLOR_BGR2RGB)
#                 faces = detector(gray)
#
#                 if len(faces) > 0:
#                     for d in faces:
#                         shape = sp(gray, d)
#                         face_descriptor = np.array(facerec.compute_face_descriptor(gray, shape))
#
#                         name = recognize_face(face_descriptor)
#                         if name != "Unknown":
#                             print(f"[SUCCESS] Face Recognized: {name}")
#                             insert_access_log("Success", name)
#
#                             if arduino:
#                                 print("[INFO] Sending unlock signal to Arduino...")
#                                 arduino.write(b'o')
#                                 time.sleep(2)
#
#                             cap.release()
#                             cv2.destroyAllWindows()
#                             exit()
#                         else:
#                             print("[ERROR] Face Recognition Failed!")
#                             insert_access_log("Failed", "Unknown")
#                             exit()
#                 else:
#                     print("[ERROR] No face detected!")
#                     insert_access_log("Failed", "No face detected")
#                     exit()
#
#         else:
#             print("[WARNING] Invalid QR Code. Please try again!")
#             incorrect_attempts += 1
#             if incorrect_attempts >= max_attempts:
#                 print("[ERROR] Too many invalid attempts! Exiting system...")
#                 cap.release()
#                 cv2.destroyAllWindows()
#                 exit()
#
#     if not found_qr:
#         print("[INFO] No QR Code detected. Waiting for valid QR...")
#
#     cv2.imshow('QR Authentication', frame)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         print("[INFO] User exited the program.")
#         break
#
# cap.release()
# cv2.destroyAllWindows()
# if arduino:
#     arduino.close()

from pymongo import MongoClient
import datetime
import cv2
import numpy as np
from pyzbar.pyzbar import decode
from faces import recognize_face, detector, sp, facerec
import time
import serial
from secret_key import key, registered_users
from db import insert_access_log

# Set up serial communication with Arduino
try:
    arduino = serial.Serial(port='COM3', baudrate=9600, timeout=1)
    if arduino:
        print("Success establishing connection with arduino")
    time.sleep(2)
except Exception as e:
    print(f"[ERROR] Could not connect to Arduino: {e}")
    arduino = None

valid_qr_data = f"Key: {key}\nRegistered Users: {', '.join(registered_users)}"
incorrect_attempts = 0
max_attempts = 3

cap = cv2.VideoCapture(0)  # Open the camera initially

while True:
    success, frame = cap.read()
    if not success:
        print("[ERROR] Camera not detected!")
        break

    found_qr = False

    for i in decode(frame):
        found_qr = True
        decoded_data = i.data.decode("utf-8").strip()
        print(f"[INFO] QR Code detected:\n{decoded_data}")

        pts = np.array([i.polygon], np.int32)
        pts = pts.reshape((-1, 1, 2))
        cv2.polylines(frame, [pts], True, (0, 255, 0), 2)
        rect_pts = i.rect
        cv2.putText(frame, "QR Scanned", (rect_pts[0], rect_pts[1]), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2)

        if decoded_data == valid_qr_data:
            print("[SUCCESS] QR Code Valid! Proceeding to face recognition...")

            cap.release()  # Close the camera temporarily
            time.sleep(5)  # Short delay before reopening

            cap = cv2.VideoCapture(0)  # Reopen the camera for face recognition

            while True:
                ret, face_frame = cap.read()
                if not ret:
                    print("[ERROR] Camera error while capturing face frame!")
                    continue

                gray = cv2.cvtColor(face_frame, cv2.COLOR_BGR2RGB)
                faces = detector(gray)

                if len(faces) > 0:
                    for d in faces:
                        shape = sp(gray, d)
                        face_descriptor = np.array(facerec.compute_face_descriptor(gray, shape))

                        name = recognize_face(face_descriptor)
                        if name in registered_users:
                            print(f"[SUCCESS] Face Recognized: {name}")
                            insert_access_log("Success", name)

                            if arduino:
                                print("[INFO] Sending unlock signal to Arduino...")
                                # arduino.write(bytes('o', 'utf-8'))
                                arduino.write("ON".encode('utf-8'))
                                time.sleep(5)
                                print("DOOR is about to be closed")
                                # arduino.write(bytes('c', 'utf-8'))  # Output the given byte string over the serial port.
                                arduino.write("OFF".encode('utf-8'))

                            cap.release()
                            cv2.destroyAllWindows()
                            exit()
                        else:
                            print(f"[ALERT] Unauthorized Face Detected: {name}")
                            insert_access_log("Anomaly", name)
                            exit()
                else:
                    print("[ERROR] No face detected!")
                    insert_access_log("Failed", "No face detected")
                    exit()

        else:
            print("[WARNING] Invalid QR Code. Please try again!")
            incorrect_attempts += 1
            if incorrect_attempts >= max_attempts:
                print("[ERROR] Too many invalid attempts! Exiting system...")
                cap.release()
                cv2.destroyAllWindows()
                exit()

    if not found_qr:
        print("[INFO] No QR Code detected. Waiting for valid QR...")

    cv2.imshow('QR Authentication', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("[INFO] User exited the program.")
        break

cap.release()
cv2.destroyAllWindows()
if arduino:
    arduino.close()
