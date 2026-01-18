
import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image
import os

MODEL_PATH = "trash_model.h5"

# 🔥 IMPORTANT CHANGE HERE
model = tf.keras.models.load_model(MODEL_PATH, compile=False)

# ⚠️ EXACT SAME ORDER AS TRAINING
CLASSES = ["dry", "e_waste", "hazardious", "wet"]

BIN_COLORS = {
    "dry": "Blue",
    "wet": "Green",
    "e_waste": "Red",
    "hazardious": "Yellow"
}

def predict_waste(img_path):
    img = image.load_img(img_path, target_size=(224, 224))
    img = image.img_to_array(img)
    img = img / 255.0
    img = np.expand_dims(img, axis=0)

    preds = model.predict(img)
    class_index = int(np.argmax(preds))

    waste = CLASSES[class_index]
    bin_color = BIN_COLORS[waste]

    return waste, bin_color
