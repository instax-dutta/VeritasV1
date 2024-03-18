from joblib import load
import pandas as pd

# --- Feature Extraction (Must match your training code)---
def extract_features(domain):
    return {
        "length": len(domain),
        "hyphens": domain.count("-"),
        "digits": sum(c.isdigit() for c in domain),
        "subdomains": domain.count("."),
        "trusted_tld": domain.split(".")[-1] in [
            "com", "org", "net", "edu", "gov", 
            "uk", "ca", "au", "de", "io", "info"  
        ]  
    }

# --- Model Loading---
model = load("phishing_detector.joblib") 

# --- Prediction Function ---
def predict_phishing(domain):
    features = pd.DataFrame([extract_features(domain)])
    prediction = model.predict(features)[0]
    if prediction == 1:
        return "Phishing Domain"
    else:
        return "Legitimate Domain"

# --- User Interaction ---
if __name__ == "__main__":
    while True: 
        user_domain = input("Enter a domain to check (or type 'quit' to exit): ")
        if user_domain.lower() == 'quit':
            break

        result = predict_phishing(user_domain)
        if result == "Phishing Domain":
            print("Warning: This domain appears to be a", result)
        else:
            print("This domain appears to be", result)
