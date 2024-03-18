**Project Title: Phishing Domain Detection Using Machine Learning**

**Overview**

This project implements a machine learning model to detect phishing domains and protect users from potential online scams.  The core components include:

*   **Feature Engineering:** A carefully designed set of features is extracted from domain names to distinguish between legitimate and phishing websites.
*   **Machine Learning Model:** A Random Forest classifier (or your chosen model) is trained on a dataset of known phishing and legitimate domains.
*   **Prediction:** The trained model is used to predict whether a new domain is likely to be a phishing attempt.

**Dataset**

*   **phishing\_domains.txt:** Contains a collection of known phishing domains.
*   **legitimate\_domains.txt:** Contains a collection of known legitimate domains.  

**Setup Instructions**

1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/instax-dutta/VeritasV1.git
    ```

2.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

**Training the Model**

1.  **Prepare Your Data (Optional):** If necessary, update `phishing_domains.txt` and `legitimate_domains.txt` with additional data.  Ensure the data quality and balance.

2.  **Run the Training Script:**
    ```bash
    python model.py
    ```
    This will train the model and save the serialized model as `phishing_detector.joblib`.

**Making Predictions**

1.  **Run the Prediction Script:**
    ```bash
    python predict.py 
    ```

2.  **Enter a domain name:**  The script will predict whether the domain is likely a phishing domain or legitimate.

**Key Features**

*   **[Feature Extraction Parameters]** 
    *   Length of domain
    *   Presence of hyphens
    *   Number of digits
    *   Subdomain count
    *   Trusted TLD check 

**Future Improvements**

*   **Expand the dataset:** Collect more diverse examples of both phishing and legitimate domains.
*   **Explore advanced features:** Incorporate lexical analysis, WHOIS lookups, and website content analysis.
*   **Experiment with different algorithms:** Evaluate the performance of other machine learning models.

**Contributions**

This project welcomes contributions!  Feel free to:

*   Report any issues or bugs you encounter.
*   Suggest new features or improvements.
*   Help expand the datasets.

**Contact**

If you have questions or want to get involved, please reach out to Abhishek Dash at bffsproductionhouse456@gmail.com 
