# import h5py
#
# model_path = "facenet_keras.h5"
# try:
#     with h5py.File(model_path, 'r') as f:
#         print("✅ Model file is valid!")
# except Exception as e:
#     print("❌ Model file is corrupted:", e)
import tensorflow as tf
from tensorflow.keras.models import load_model

model_path = "facenet_keras.h5"

try:
    facenet = load_model(model_path, compile=False)  # Ensure compile=False
    facenet.save("facenet_saved_model")  # Convert to SavedModel format
    print("✅ Model converted to SavedModel format!")

    # Load from the new format
    facenet = tf.keras.models.load_model("facenet_saved_model")
    print("✅ Model reloaded successfully from SavedModel format!")
except Exception as e:
    print("❌ Error:", e)
