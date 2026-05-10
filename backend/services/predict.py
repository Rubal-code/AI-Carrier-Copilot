import os
import joblib

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

model = joblib.load(os.path.join(BASE_DIR, "../../ml/saved_models/model.pkl"))

vectorizer = joblib.load(os.path.join(BASE_DIR, "../../ml/saved_models/vectorizer.pkl"))
    
label_encoder = joblib.load(os.path.join(BASE_DIR, "../../ml/saved_models/encoder.pkl"))


def predict_role(skills):

    text = " ".join(skills)

    vec = vectorizer.transform([text])

    pred = model.predict(vec)

    role = label_encoder.inverse_transform(pred)

    return role[0]