# Alternative if you want to inspect pre-flattened data
import pandas as pd
import requests

url = "https://fakestoreapi.com/products"
response = requests.get(url)
data = response.json()

df = pd.DataFrame(data)

print(df.head())
print(type(df['rating'][0]))
