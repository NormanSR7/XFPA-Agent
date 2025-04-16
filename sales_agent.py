import requests # Library to make API calls
import pandas as pd # Places data into a dataframe

# Step 1: Define the API endpoint
url = "https://fakestoreapi.com/products"

# Step 2: Use the requests to pull the data
response = requests.get(url)

# Step 3: Check the response
if response.status_code == 200:
    data = response.json()
    print(f"Fetched {len(data)} products.")
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")

# Step 4: Convert JSON to pandas Dataframe
df = pd.DataFrame(data)

# Step 5: Preview the Dataframe
print("\nSample Data")
print(df.head())