import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.utils import resample 
from joblib import dump

# --- Feature Extraction ---
def extract_features(domain):
    parts = domain.split("://")
    has_protocol = len(parts) > 1

    return {
        "length": len(domain),
        "hyphens": domain.count("-"),
        "digits": sum(c.isdigit() for c in domain),
        "subdomains": domain.count("."),
        "trusted_tld": domain.split(".")[-1] in [
            "com", "org", "net", "edu", "gov", 
            "uk", "ca", "au", "de", "io", "info"  
        ],  
        "has_protocol": has_protocol  
    }

# --- Paths and Configuration ---
phishing_data_dir = "divided"  # Replace with your actual path
legitimate_domains_file = "legitimate_domains.txt"  
model_output_file = "phishing_detector.joblib" 
accuracy_threshold = 0.95

# --- Load Legitimate Domains ---
with open(legitimate_domains_file, "r") as file:
    legitimate_domains = file.read().splitlines()

# --- Iterative Training ---
for file_num in range(1, 2573):  
    file_name = f"domains_{file_num}.txt"
    file_path = os.path.join(phishing_data_dir, file_name)

    with open(file_path, "r") as file:
        phishing_domains = file.read().splitlines()

    # --- Data Preprocessing ---
    data = pd.DataFrame([extract_features(d) for d in phishing_domains + legitimate_domains])
    labels = pd.Series([1] * len(phishing_domains) + [0] * len(legitimate_domains))  

    # Encode categorical features
    encoder = LabelEncoder()
    data['trusted_tld'] = encoder.fit_transform(data['trusted_tld']) 

    # Oversampling Legitimate URLs
    df_legitimate = data[labels == 0].sample(n=len(phishing_domains), replace=True)
    data = pd.concat([df_legitimate, data[labels == 1]])
    labels = pd.Series([0] * len(df_legitimate) + [1] * len(phishing_domains)) 

    # Split into train/test
    X_train, X_test, y_train, y_test = train_test_split(data, labels, test_size=0.2, random_state=42)

    # Train and Evaluate Model
    model = RandomForestClassifier(n_estimators=100, random_state=42) 
    model.fit(X_train, y_train)
    accuracy = model.score(X_test, y_test)

    print(f"Accuracy after training on domains_{file_num}.txt: {accuracy}")
    if accuracy >= accuracy_threshold:
        dump(model, model_output_file)  

# --- Dataset Source Suggestions ---
# * DMOZ Directory (archived): https://en.wikipedia.org/wiki/DMOZ
# * Common Crawl: https://commoncr                                                                                                                                                                             awl.org/
# * Search for publicly available "legitimate URL datasets" 
