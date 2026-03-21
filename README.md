# Smart Cyberattack Detection Using AI and NLP

An intelligent cybersecurity system designed to **detect SQL Injection attacks** using **Artificial Intelligence (AI) and Natural Language Processing (NLP)** techniques.

---

## Overview

SQL Injection is one of the most critical threats to web applications, allowing attackers to manipulate databases and access sensitive information.

This project introduces a **smart detection system** that analyzes SQL queries and classifies them as:

*  Normal Queries
*  SQL Injection Attacks

The system leverages **machine learning and NLP techniques** to improve detection accuracy and reduce false positives.

---

## Problem Statement

Traditional SQL Injection detection systems:

* Depend on predefined rules or signatures
* Fail to detect new or complex attack patterns
* Produce high false positives and false negatives

This makes them unreliable for modern cybersecurity needs.

---

## Proposed Solution

This project proposes an **AI-based detection system** that:

* Analyzes query patterns using NLP techniques
* Extracts meaningful features using **Bag-of-Words (BoW)**
* Uses **Random Forest Classifier** for accurate classification
* Compares performance with other ML algorithms

---

## Key Features

✔ AI-based SQL Injection detection

✔ NLP-based feature extraction

✔ Real-time query classification

✔ Comparison with multiple ML algorithms

✔ User-friendly GUI using Tkinter

✔ High accuracy with reduced false results

---

## Methodology

### 1. Data Collection

* Dataset containing:

  * Normal SQL queries
  * SQL Injection queries

### 2. Data Preprocessing

* Remove special characters
* Convert text to lowercase
* Clean and normalize query data

### 3. Feature Extraction

* Use **Regular Expressions** to identify patterns
* Apply **Bag-of-Words (BoW)** model to convert text into numerical features

### 4. Model Training

* Train **Random Forest Classifier**
* Compare with:

  * SVM
  * KNN
  * Naive Bayes
  * Decision Tree

### 5. Evaluation

* Accuracy
* Precision
* Recall
* F1-Score

---

## Technologies Used

### Programming

* **Python**

### Machine Learning

* **Scikit-learn**
* **Random Forest Classifier**

### NLP Techniques

* **Bag-of-Words (BoW)**
* **Regular Expressions**

### Data Handling

* **Pandas**
* **NumPy**

### Visualization

* **Matplotlib**

### Interface

* **Tkinter (GUI)**

---

## Project Structure

smart-cyberattack-detection

├── dataset/              # SQL queries dataset (normal & injection)

├── ipd2.11code.py        # Main application (Tkinter GUI)

└── README.md             # Project documentation

---

## Dataset

The dataset contains labeled SQL queries:

* **Normal Queries**
* **SQL Injection Queries**

### Dataset Columns:

* `payload` → SQL query
* `label` → Classification (Normal / Injection)

### Purpose:

* Train machine learning models
* Identify malicious patterns
* Improve detection accuracy

---

## How It Works

1. Upload dataset
2. Preprocess and clean data
3. Extract features using NLP techniques
4. Train machine learning models
5. Evaluate model performance
6. Predict whether a query is:

   * Normal
   * SQL Injection

---

## Results

* Random Forest achieved **higher accuracy** compared to other algorithms
* Reduced false positives and false negatives
* Effective in detecting both simple and complex SQL Injection attacks

---

## Key Highlights

* Combines **AI + NLP + Cybersecurity**
* Practical real-world application
* GUI-based system for easy usage
* Comparative analysis of ML algorithms
* Scalable for real-time applications

---

## Future Enhancements

* Integration with real-time web applications
* Deep learning models for improved accuracy
* Real-time attack detection systems
* Larger and more diverse datasets
* Deployment as a web security tool

---

## Conclusion

This project demonstrates how **AI and NLP techniques can significantly enhance cybersecurity systems**, providing a robust solution for detecting SQL Injection attacks and improving web application security.

---

## Authors

**K. Anusha**

