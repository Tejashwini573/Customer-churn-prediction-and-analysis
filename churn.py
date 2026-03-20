# Netflix Customer Churn Prediction Project

# Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

sns.set(style="whitegrid")


# Load Dataset
df = pd.read_csv("netflix_customer_churn.csv")
# Fix churn column values
df['churned'] = df['churned'].replace({
    'Yes': 1,
    'No': 0
})

# Ensure churn column is binary
df['churned'] = df['churned'].astype(int)
print(df['churned'].value_counts())
print("First 5 rows:")
print(df.head())

print("\nDataset Shape:", df.shape)

print("\nDataset Info:")
print(df.info())

print("\nStatistical Summary:")
print(df.describe())


# Data Cleaning

df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

df = df.drop_duplicates()

for col in df.select_dtypes(include="object").columns:
    df[col] = df[col].str.strip()


print("\nMissing Values:")
print(df.isnull().sum())


# Handle Missing Values

num_cols = df.select_dtypes(include=['int64','float64']).columns
df[num_cols] = df[num_cols].fillna(df[num_cols].median())

cat_cols = df.select_dtypes(include='object').columns

for col in cat_cols:
    df[col].fillna(df[col].mode()[0], inplace=True)

print("\nData Cleaning Completed")


# Feature Engineering

df['churn_status'] = df['churned'].apply(lambda x: "Churned" if x == 1 else "Active")


# Customer Summary

total_customers = len(df)
churned_customers = df[df['churned']==1].shape[0]
active_customers = df[df['churned']==0].shape[0]

churn_rate = (churned_customers / total_customers) * 100

print("\nCustomer Summary")
print("Total Customers:", total_customers)
print("Active Customers:", active_customers)
print("Churned Customers:", churned_customers)
print("Churn Rate:", round(churn_rate,2), "%")


# EDA VISUALIZATIONS (Reduced & Important)


# 1 Churn Distribution
sns.countplot(x='churn_status', data=df)
plt.title("Customer Churn Distribution")
plt.show()


# 2 Churn by Subscription Type
plt.figure(figsize=(7,5))
sns.countplot(x='subscription_type', hue='churn_status', data=df)
plt.title("Churn by Subscription Type")
plt.show()


# 3 Watch Hours vs Churn
plt.figure(figsize=(7,5))
sns.boxplot(x='churn_status', y='watch_hours', data=df)
plt.title("Watch Hours vs Churn")
plt.show()


# 4 Last Login Days vs Churn
plt.figure(figsize=(7,5))
sns.boxplot(x='churn_status', y='last_login_days', data=df)
plt.title("Last Login Days vs Churn")
plt.show()


# 5 Churn by Region
plt.figure(figsize=(8,5))
sns.countplot(x='region', hue='churn_status', data=df)
plt.title("Churn by Region")
plt.xticks(rotation=45)
plt.show()


# 6 Correlation Heatmap
plt.figure(figsize=(10,6))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm")
plt.title("Feature Correlation Matrix")
plt.show()


# Machine Learning Model

df_model = df.copy()

le = LabelEncoder()

for col in df_model.select_dtypes(include='object').columns:
    df_model[col] = le.fit_transform(df_model[col])


X = df_model.drop(['churned','churn_status'], axis=1)
y = df_model['churned']


X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


model = LogisticRegression(max_iter=1000)

model.fit(X_train, y_train)


y_pred = model.predict(X_test)


print("\nModel Accuracy:", accuracy_score(y_test, y_pred))

print("\nConfusion Matrix")
print(confusion_matrix(y_test, y_pred))

print("\nClassification Report")
print(classification_report(y_test, y_pred))
from sklearn.metrics import ConfusionMatrixDisplay
ConfusionMatrixDisplay.from_predictions(y_test, y_pred)
plt.title("Confusion Matrix")
plt.show()


# Feature Importance

importance = pd.Series(model.coef_[0], index=X.columns)
importance = importance.sort_values()

plt.figure(figsize=(8,6))
importance.plot(kind='barh')
plt.title("Feature Importance for Churn Prediction")
plt.show()


# Identify High Risk Customers

df['churn_probability'] = model.predict_proba(X)[:,1]

high_risk_customers = df.sort_values(
    by='churn_probability', ascending=False
).head(10)

print("\nTop 10 Customers Most Likely to Churn:")
print(high_risk_customers[['customer_id','churn_probability']])


# Save Clean Dataset

df.to_csv("Cleaned_churn_dataset.csv", index=False)

print("\nCleaned dataset saved successfully.")