import pandas as pd
import requests
from sqlalchemy import create_engine
import os

# Step 1: Pull the data using requests
url = "https://fakestoreapi.com/products"
response = requests.get(url)
data = response.json()

# Step 2: Convert to a dataframe
df = pd.DataFrame(data)

# Flatten the 'rating' column
df['rating_rate'] = df['rating'].apply(lambda x: x['rate'])
df['rating_count'] = df['rating'].apply(lambda x: x['count'])
df.drop(columns=['rating'], inplace=True)

# Step 3: Create the database
db_path = "xfpa.db"
engine = create_engine(f"sqlite:///{db_path}")

# Step 4: Save to SQL table
df.to_sql("products",engine, if_exists="replace", index=False)

# Step 5: Confirm
print("✅ Data saved to SQL successfully!")
print("Database location:",os.path.abspath(db_path))
