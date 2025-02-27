# import os
# import pickle
# import numpy as np
# from PIL import Image
# import cv2
#
# # Load the Haar Cascade for face detection
# face_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_alt2.xml')
#
# # Get the base directory of the script
# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# image_dir = os.path.join(BASE_DIR, 'images')
# print("Image dir:", image_dir)
#
# # Initialize variables
# image_id = 0
# label_id = {}
# y_train_label = []
# x_train_data = []
#
#
# # Iterate through all image files in the dataset
# def process_images():
#     global image_id
#     for root, dirs, files in os.walk(image_dir):
#         print(root, dirs, files)
#         for file in files:
#             if file.endswith(('png', 'jpg', 'jpeg')):
#                 path = os.path.join(root, file)
#                 label = os.path.basename(root).replace(' ', '_').lower()
#
#                 if label not in label_id:  # Assign numerical labels
#                     label_id[label] = image_id
#                     image_id += 1
#
#                 # Open image, convert to grayscale
#                 pil_image = Image.open(path).convert('L')
#                 size = (400, 533)  # Resize for consistency
#                 final_image = pil_image.resize(size, Image.LANCZOS)
#                 image_array = np.array(final_image)
#
#                 # Detect faces
#                 faces = face_cascade.detectMultiScale(image_array, scaleFactor=1.1, minNeighbors=7)
#                 if len(faces) > 0:
#                     for (x, y, w, h) in faces:
#                         roi_gray = image_array[y:y + h, x:x + w]  # Extract face region
#
#                         # Normalize face data
#                         roi_gray = cv2.resize(roi_gray, (100, 100))
#                         roi_gray = cv2.equalizeHist(roi_gray)  # Improve contrast
#
#                         y_train_label.append(label_id[label])
#                         x_train_data.append(roi_gray)
#                 else:
#                     print(f"Warning: No face detected in {file}, skipping...")
#
#
# # Process images
# process_images()
#
# # Check if training data is collected
# if len(x_train_data) == 0:
#     print("Error: No valid face data found. Ensure images contain detectable faces.")
#     exit()
#
# # Save label mappings
# with open('label_ids.pickle', 'wb') as fw:
#     pickle.dump(label_id, fw)
#
# # Train the recognizer
# recognizer = cv2.face.LBPHFaceRecognizer_create()
# recognizer.train(np.array(x_train_data, dtype=np.uint8), np.array(y_train_label))
# recognizer.save('trainer.yml')
#
# print("Training complete. Model saved as 'trainer.yml'.")
# print(f"Label mapping: {label_id}")

#
# import os
# import pickle
# import numpy as np
# from PIL import Image
# import cv2
#
# # Load the Haar Cascade for face detection
# face_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_alt2.xml')
#
# # Get the base directory of the script
# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# image_dir = os.path.join(BASE_DIR, 'images')
# print("Image Directory:", image_dir)
#
# # Initialize variables
# image_id = 0
# label_id = {}  # Mapping of label names to numeric IDs
# y_train_label = []  # Store label IDs
# x_train_data = []  # Store processed face images
#
#
# def process_images():
#     """ Process all images in the dataset folder and extract face regions. """
#     global image_id
#     for root, dirs, files in os.walk(image_dir):
#         print(f"Processing directory: {root} ({len(files)} files found)")
#         for file in files:
#             if file.lower().endswith(('png', 'jpg', 'jpeg')):
#                 path = os.path.join(root, file)
#                 label = os.path.basename(root).replace(' ', '_').lower()
#
#                 # Assign unique ID to each person (label)
#                 if label not in label_id:
#                     label_id[label] = image_id
#                     image_id += 1
#
#                 # Open image, convert to grayscale
#                 try:
#                     pil_image = Image.open(path).convert('L')
#                 except Exception as e:
#                     print(f"Error loading image {file}: {e}")
#                     continue
#
#                 size = (400, 533)  # Resize for consistency
#                 final_image = pil_image.resize(size, Image.LANCZOS)
#                 image_array = np.array(final_image, dtype=np.uint8)
#
#                 # Detect faces
#                 faces = face_cascade.detectMultiScale(image_array, scaleFactor=1.1, minNeighbors=6, minSize=(30, 30))
#
#                 if len(faces) > 0:
#                     for (x, y, w, h) in faces:
#                         roi_gray = image_array[y:y + h, x:x + w]  # Extract face region
#
#                         # Normalize face data (Resize & Equalize)
#                         roi_gray = cv2.resize(roi_gray, (100, 100))
#                         roi_gray = cv2.equalizeHist(roi_gray)  # Improve contrast
#
#                         y_train_label.append(label_id[label])
#                         x_train_data.append(roi_gray)
#                 else:
#                     print(f"⚠️ Warning: No face detected in {file}, skipping...")
#
#
# # Process images
# process_images()
#
# # Check if training data is available
# if len(x_train_data) == 0:
#     print("❌ Error: No valid face data found. Ensure images contain detectable faces.")
#     exit()
#
# # Save label mappings
# with open('label_ids.pickle', 'wb') as fw:
#     pickle.dump(label_id, fw)
#
# # Train the LBPH recognizer
# recognizer = cv2.face.LBPHFaceRecognizer_create()
# recognizer.train(np.array(x_train_data, dtype=np.uint8), np.array(y_train_label))
# recognizer.save('trainer.yml')
#
# print("\n✅ Training complete. Model saved as 'trainer.yml'.")
# print(f"📌 Label mapping: {label_id}")


#testing for better accuracy
import os
import pickle
import numpy as np
import cv2
import dlib
import yaml
from PIL import Image

# Define paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
image_dir = os.path.join(BASE_DIR, 'images')

# Load face detector and face embedding model (Dlib's ResNet)
detector = dlib.get_frontal_face_detector()
sp = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
facerec = dlib.face_recognition_model_v1("dlib_face_recognition_resnet_model_v1.dat")

# Initialize variables
label_id = {}
image_id = 0
x_train_data = []
y_train_label = []


# Process images
def process_images():
    global image_id
    for root, dirs, files in os.walk(image_dir):
        for file in files:
            if file.endswith(('png', 'jpg', 'jpeg')):
                path = os.path.join(root, file)
                label = os.path.basename(root).replace(' ', '_').lower()

                if label not in label_id:
                    label_id[label] = image_id
                    image_id += 1

                # Open image and convert to grayscale
                pil_image = Image.open(path).convert('RGB')
                image_array = np.array(pil_image)

                # Detect faces
                detections = detector(image_array)

                if len(detections) > 0:
                    for d in detections:
                        shape = sp(image_array, d)
                        face_descriptor = facerec.compute_face_descriptor(image_array, shape)

                        y_train_label.append(label_id[label])
                        x_train_data.append(face_descriptor)
                else:
                    print(f"⚠️ No face detected in {file}, skipping...")


# Process the dataset
process_images()

# Ensure data is collected
if len(x_train_data) == 0:
    print("❌ Error: No valid face data found.")
    exit()

# Save data to training.yml
train_data = {
    "labels": label_id,
    "embeddings": [list(embedding) for embedding in x_train_data],
    "label_ids": y_train_label
}

with open("trainer.yml", "w") as f:
    yaml.dump(train_data, f)

print("✅ Face embeddings saved in 'trainer.yml'.")
print(f"📌 Label mapping: {label_id}")
