import pandas as pd
from sqlalchemy import create_engine

# Connect to the existing SQLite database
engine = create_engine("sqlite:///xfpa.db")

# Query everything from the products table
df = pd.read_sql("SELECT * FROM products",engine)

# Show all rows and columns
pd.set_option('display.max_rows',None)
pd.set_option('display.max_columns',None)

# Save to csv
df.to_csv("products_export.csv",index=False)
print("Exported to products_export.csv")


# Print the full table
print(df)


