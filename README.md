# Customer-churn-prediction-and-analysis

📌 Project Overview

Customer churn is a critical challenge for subscription-based businesses, as losing customers directly impacts revenue and growth. This project aims to analyze customer behavior and build a predictive model to identify customers who are likely to churn.

The project follows an end-to-end data analytics workflow, starting from data cleaning and exploration to machine learning model development and visualization of insights.

🎯 Objectives

Analyze customer data to identify patterns and trends influencing churn

Perform data preprocessing and transformation for accurate analysis

Build a machine learning model to predict customer churn

Evaluate model performance using standard metrics

Provide actionable insights to improve customer retention

🛠️ Tools & Technologies

Programming Language: Python

Libraries: Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn

Visualization: Power BI

Database/Querying: SQL

📂 Dataset Description

The dataset contains customer information such as:

Customer demographics

Subscription type (Basic, Standard, Premium)

Watch hours / engagement level

Last login activity

Region

Churn status (Target variable)

🧹 Data Preprocessing

Handled missing and inconsistent values

Converted categorical variables into numerical format using encoding

Standardized data types for analysis

Transformed churn column into binary values (Yes → 1, No → 0)

📊 Exploratory Data Analysis (EDA)

EDA was performed to uncover meaningful patterns and relationships:

Distribution of churn vs active customers

Churn by subscription type

Impact of watch hours on churn

Relationship between last login activity and churn

Regional churn distribution

Correlation analysis using heatmaps

📌 Key Insight: Customers with low engagement (low watch hours & longer inactivity) showed a higher probability of churn.

🤖 Machine Learning Model

Model Used: Logistic Regression

Process:

Split dataset into training and testing sets

Trained model using Scikit-learn

Predicted churn probabilities

📈 Model Evaluation

The model was evaluated using:

Accuracy Score – Measures overall correctness

Confusion Matrix – Shows prediction breakdown

Classification Report – Includes precision, recall, and F1-score

📌 The model demonstrates effective performance in identifying churn patterns and classifying customers.

📊 Dashboard & Visualization

An interactive Power BI dashboard was created to present:

Churn rate and key KPIs

Customer segmentation

Engagement analysis

Regional trends

This helps stakeholders quickly understand insights and make data-driven decisions.

💡 Key Insights

Low user engagement is a major indicator of churn

Customers inactive for longer periods are more likely to leave

Subscription type influences churn behavior

Certain regions show higher churn rates

🚀 Conclusion

This project successfully demonstrates how data analysis and machine learning can be used to predict customer churn and generate actionable business insights. The results can help companies improve retention strategies, enhance customer experience, and reduce revenue loss.

🔮 Future Improvements

Use advanced models (Random Forest, XGBoost) for better accuracy

Hyperparameter tuning for optimization

Deployment using Flask/Streamlit

Real-time churn prediction system
