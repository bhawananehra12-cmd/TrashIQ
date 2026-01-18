from flask import Flask, request, jsonify
from flask_cors import CORS
import os, uuid, traceback

# Maan lete hain ki predict_waste aapke model se result lata hai
from predict import predict_waste 

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/predict", methods=["POST"])
def predict():
    path = None
    try:
        if "image" not in request.files:
            return jsonify({"error": "No image"}), 400

        file = request.files["image"]
        ext = os.path.splitext(file.filename)[1]
        filename = f"{uuid.uuid4().hex}{ext}"
        path = os.path.join(UPLOAD_FOLDER, filename)
        
        # Save and close the file properly
        file.save(path)
        file.close() 

        # Prediction logic
        waste, bin_color = predict_waste(path)

        # File delete kar rahe hain taaki memory na bhare (Unlimited uploads ke liye)
        if os.path.exists(path):
            os.remove(path)

        return jsonify({
            "waste_type": waste,
            "bin_color": bin_color,
            "message": "Thank you for protecting the environment 🌱"
        })

    except Exception:
        if path and os.path.exists(path):
            os.remove(path) # Error aane par bhi file delete karein
        traceback.print_exc()
        return jsonify({"error": "Prediction failed"}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    