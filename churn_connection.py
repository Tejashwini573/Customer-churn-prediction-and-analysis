import pandas as pd
from sqlalchemy import create_engine

print("Step 1: Starting program")

# Load CSV
df = pd.read_csv("netflix_customer_churn.csv")
print("Step 2: CSV Loaded")
print("Rows in dataset:", len(df))

# Connect to MySQL
engine = create_engine("mysql+pymysql://root:Trhubli%40123@localhost/netflix_customer_churn")
print("Step 3: Database Connected")

# Insert data
print("Step 4: Inserting data into MySQL...")

df.to_sql(
    name="customer_churn_data",
    con=engine,
    if_exists="replace",
    index=False,
    chunksize=1000,
    method="multi"
)

print("Step 4: Data inserted successfully")

# Verify
result = pd.read_sql("SELECT COUNT(*) AS total_rows FROM customer_churn_data", engine)

print("Step 5: Data verification")
print(result)