# #qr and face recognition authentication as two different independent modules
# import cv2
# import numpy as np
# from pyzbar.pyzbar import decode   #pyzbar helps in detection and decoding of the qrcode
# from faces import face_recognition
#
# cap=cv2.VideoCapture(0)
#
#
#
# while(True):
#     success,frame=cap.read()
#
#     for i in decode(frame):
#         decoded_data=i.data.decode("utf-8")   #converts bytes to string value
#         print(decoded_data)
#
#         #Drawing polygon on frame (tilts w.r.t orientation)
#         pts=np.array([i.polygon],np.int32)
#
#         pts=pts.reshape((-1,1,2))
#         cv2.polylines(frame,[pts],True,(0,0,255),2)
#         # print(pts)
#
#         #Display text
#         rect_pts=i.rect #using rect point as origin for text as we don't want the text to tilt with the qrcode
#         fontScale=0.8
#         thickness=1
#         cv2.putText(frame,decoded_data,(rect_pts[0],rect_pts[1]),cv2.FONT_HERSHEY_SIMPLEX,fontScale,(255,0,0),thickness)
#         # print(rect_pts)
#
#         if(decoded_data.lower()=="barcelona"):
#             cap.release()
#             cv2.destroyAllWindows()
#             face_recognition()
#
#     cv2.imshow('Result',frame)
#
#     ch=cv2.waitKey(1) #delay of 1ms
#     if(ch==113):
#         break
#

import cv2
import numpy as np
from pyzbar.pyzbar import decode   # Pyzbar helps in detection and decoding of the QR code
from faces import face_recognition
import time
from secret_key import key, registered_users  # Import key and registered users

cap = cv2.VideoCapture(0)

# Generate the expected QR data format
valid_qr_data = f"Key: {key}\nRegistered Users: {', '.join(registered_users)}"

# Counter for incorrect attempts
incorrect_attempts = 0
max_attempts = 3  # Set a limit for invalid QR scans

while True:
    success, frame = cap.read()

    if not success:
        print("[ERROR] Camera not detected!")
        break

    found_qr = False  # Flag to check if a QR code is detected in the frame

    for i in decode(frame):
        found_qr = True  # QR code found in the frame
        decoded_data = i.data.decode("utf-8").strip()  # Converts bytes to string value
        print(f"[INFO] QR Code detected:\n{decoded_data}")

        # Drawing polygon around the QR code
        pts = np.array([i.polygon], np.int32)
        pts = pts.reshape((-1, 1, 2))
        cv2.polylines(frame, [pts], True, (0, 255, 0), 2)  # Green polygon for detected QR

        # Display decoded text
        rect_pts = i.rect  # Using rect point for text display
        font_scale = 0.8
        thickness = 2
        cv2.putText(frame, "QR Scanned", (rect_pts[0], rect_pts[1]), cv2.FONT_HERSHEY_SIMPLEX, font_scale, (255, 0, 0), thickness)

        # Check if QR code is valid
        if decoded_data == valid_qr_data:
            print("[SUCCESS] QR Code Valid! Proceeding to face recognition...")
            cap.release()
            cv2.destroyAllWindows()
            face_recognition()
            exit()
        else:
            print(f"[WARNING] Invalid QR Code. Please try again!")
            incorrect_attempts += 1
            if incorrect_attempts >= max_attempts:
                print("[ERROR] Too many invalid attempts! Exiting system...")
                cap.release()
                cv2.destroyAllWindows()
                exit()

    # If no QR code is found, print a message
    if not found_qr:
        print("[INFO] No QR Code detected. Waiting for valid QR...")

    cv2.imshow('QR Authentication', frame)

    # Exit on pressing 'q'
    ch = cv2.waitKey(1) & 0xFF
    if ch == ord('q'):
        print("[INFO] User exited the program.")
        break

# Cleanup
cap.release()
cv2.destroyAllWindows()
