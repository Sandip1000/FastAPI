import pickle
import pandas as pd


# Import The ML Model
with open(fr"model/model.pkl", "rb") as f:
    model = pickle.load(f)

# MLFlow
MODEL_VERSION = "1.0.0"

# Get class labels from model (important for matching probablities to class name)
class_labels = model.classes_.tolist()

def predict_output(user_input : dict):
    
    input_df = pd.DataFrame([user_input])

    # Predict the class 
    predicted_class = model.predict(input_df)[0]

    # Get the probalities for all classes
    probabilities = model.predict_proba(input_df)[0]
    confidence = max(probabilities)

    # Create mapping: {class_name : probalility}
    class_probs = dict(zip(class_labels, map(lambda p: round(p,4), probabilities)))

    return {
        "predicted_category" : predicted_class,
        "confidence" : round(confidence, 4),
        "class_probabilities" : class_probs
    }