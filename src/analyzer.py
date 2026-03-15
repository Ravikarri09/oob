from urllib.parse import urlparse, parse_qs
import pickle
from src.oob_detector import detect_oob

model = pickle.load(open("model/sqli_model.pkl", "rb"))
vectorizer = pickle.load(open("model/vectorizer.pkl", "rb"))

def extract_payload(input_data):

    if "http" in input_data:
        parsed = urlparse(input_data)
        params = parse_qs(parsed.query)

        payload = " ".join([v[0] for v in params.values()])
        return payload

    return input_data


def analyze_payload(input_data):

    payload = extract_payload(input_data)

    data = vectorizer.transform([payload])

    prediction = model.predict(data)[0]

    oob = detect_oob(payload)

    if prediction == 1:
        ml_result = "Malicious"
    else:
        ml_result = "Safe"

    if oob:
        oob_result = "Possible OOB SQL Injection"
    else:
        oob_result = "No OOB detected"

    return {
        "Payload": payload,
        "ML_Detection": ml_result,
        "OOB_SQLi": oob_result
    }