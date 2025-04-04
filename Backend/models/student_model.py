import joblib
import numpy as np
from pathlib import Path


class StudentLevelPredictor:
    def __init__(self):
        model_dir = Path(__file__).parent
        self.model = joblib.load(model_dir / "xgboost_model.joblib")
        self.scaler = joblib.load(model_dir /"scaler.joblib")
        self.label_encoders = joblib.load(model_dir /"label_encoders.joblib")
        self.features = joblib.load(model_dir /"features.joblib")

    def predict_level(self, knowledge_level, learning_speed):
        # Encode input features
        encoded_knowledge = self.label_encoders["Knowledge_Level"].transform(
            [knowledge_level]
        )[0]
        encoded_speed = self.label_encoders["Learning_Speed"].transform(
            [learning_speed]
        )[0]

        # Create feature array
        X = np.array([[encoded_knowledge, encoded_speed]])

        # Scale features
        X_scaled = self.scaler.transform(X)

        # Get prediction and probabilities
        prediction = self.model.predict(X_scaled)[0]
        probabilities = self.model.predict_proba(X_scaled)[0]

        # Get confidence score
        confidence = probabilities[prediction]

        # Decode prediction back to original label
        next_level = self.label_encoders["Next_Level"].inverse_transform([prediction])[
            0
        ]

        return {"next_level": next_level, "confidence": float(confidence)*2.2}
