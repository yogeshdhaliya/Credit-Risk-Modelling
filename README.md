# 🏦 Credit Risk Prediction Application

A machine learning-powered web application for real-time credit risk assessment.

-----

## 🌟 1. Short Description

This project provides an interactive web application built with **Streamlit** to predict the credit risk of a loan applicant. It utilizes a pre-trained **Extra Trees Classifier** model, trained on the **German Credit Data** dataset, to classify new applicants as having a **Good** (Lower Risk) or **Bad** (Higher Risk) credit profile.

## 🎯 2. Problem Statement

Financial institutions and banks face the crucial challenge of accurately assessing the risk associated with lending capital. Inaccurate credit decisions can lead to significant financial losses from defaults. This project addresses this by developing a robust, transparent Machine Learning model to automate and optimize the credit risk evaluation process, enabling faster and more informed lending decisions.

-----

## ✨ 3. Features

  * **Interactive Streamlit UI:** A user-friendly interface for inputting applicant details.
  * **Real-Time Prediction:** Instantaneous credit risk prediction (**Good** or **Bad**) upon clicking the 'Predict' button.
  * **Extra Trees Classifier:** A high-performance ensemble model is used as the core predictive engine.
  * **Data Visibility:** Displays the encoded input data in a pandas DataFrame to show the exact values fed into the model.
  * **Categorical Encoding:** Uses pre-fitted `LabelEncoder` objects for consistent feature transformation.

-----

## 📦 4. Technologies Used

| Category | Technology | Purpose |
| :--- | :--- | :--- |
| **Language** | Python | Primary programming language |
| **Framework** | Streamlit | Web application development and deployment |
| **ML Libraries** | Scikit-learn | Model training (ExtraTreesClassifier), evaluation, and preprocessing (LabelEncoder) |
| **Data Handling** | Pandas, NumPy | Data manipulation and feature engineering |
| **Persistence** | Joblib | Serialization and loading of the model and encoders |

The dataset used for training is the **German Credit Data** (`german_credit_data.csv`).

-----

## 🛠️ 5. Installation Instructions

To set up and run this project locally, follow these steps:

### Prerequisites

You need **Python 3.8+** installed on your system.

### Step 1: Clone the Repository

```bash
git clone [YOUR_REPOSITORY_URL_HERE]
cd [YOUR_REPOSITORY_NAME]
```

### Step 2: Install Dependencies

All required Python libraries are listed in `requirements.txt`.

```bash
pip install -r requirements.txt
```

### Step 3: Run the Streamlit Application

Execute the `app.py` file using Streamlit:

```bash
streamlit run app.py
```

The application will automatically open in your default web browser at `http://localhost:8501`.

-----

## 🚀 6. Usage

1.  Open the Streamlit application (either locally or using the deployed URL).
2.  Enter the required loan applicant details, such as **Age**, **Job**, **Credit Amount**, **Duration**, **Housing**, and **Account Statuses**.
3.  Review the **Input Data for Model** table to see the encoded values that will be used.
4.  Click the **"Predict Credit Risk"** button to view the final prediction (**GOOD** or **BAD**).

-----

## 🌐 7. App / Streamlit URL

The live application is deployed and available here:

[Credit Risk Modelling by Yogesh](https://credit-risk-modelling-by-yogesh.streamlit.app/)

-----

## 📸 8. Screenshots or Demo

| Prediction Page | Input Data Visualization |
| :---: | :---: |
|  |  |

-----

## 🤝 9. Contributing

If you'd like to contribute, please fork the repository and use a feature branch. Pull requests are warmly welcome.

-----

## 📄 10. License

This project is licensed under the **[MIT License / Apache 2.0 / Choose License]** - see the `LICENSE.md` file for details.

-----

## ✉️ 11. Contact / Author Info

| Role | Details |
| :--- | :--- |
| **Author** | [Your Name / GitHub Username] |
| **GitHub** | [Your GitHub Profile Link] |
| **Email** | [Your Email Address] |
