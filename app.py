from src.analyzer import analyze_payload
from src.oob_detector import detect_oob
while True:

    payload = input("\nEnter SQL Payload (or type exit): ")

    if payload.lower() == "exit":
        break

    result = analyze_payload(payload)

    print("\nAnalysis Result:")
    print(result)