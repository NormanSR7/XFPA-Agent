import pandas as pd
from sqlalchemy import create_engine

# Connect to the local database
engine = create_engine("sqlite:///xfpa.db")

# Read the full products table
df = pd.read_sql("SELECT * FROM products", engine)

# Preview the full table
print("\n All Products:")
print(df.head())

# Query - Filter products over R500
expensive_df = pd.read_sql("SELECT * FROM products WHERE price > 500", engine)
print("\n Expensive Products:")
print(expensive_df.head())

# Query - Sort by rating
sorted_df = pd.read_sql("SELECT * FROM products ORDER BY rating_rate DESC", engine)
print("\n⭐ Top Rated Products:")
print(sorted_df[['title', 'rating_rate']].head())