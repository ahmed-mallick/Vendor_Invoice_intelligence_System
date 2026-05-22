import joblib
import pandas as pd

MODEL_PATH = "models/predict_freight_model.pkl"

def load_model(model_path: str = MODEL_PATH):
    with open(model_path, "rb") as f:
        model = joblib.load(f)
    return model

def predict_freight_cost(input_data):
    model = load_model()
    input_df = pd.DataFrame(input_data)
    input_df = input_df.rename(columns={"Invoice_Dollars": "Dollars"})
    input_df = input_df[["Dollars"]]
    predictions = model.predict(input_df).round()
    return float(predictions.flatten()[0])
