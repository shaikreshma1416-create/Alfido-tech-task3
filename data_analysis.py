import pandas as pd
import numpy as np

# Load data
df = pd.read_csv("data.csv")

# View data
print(df.head())
print(df.info())

# Missing values
print(df.isnull().sum())

# Clean data
for col in df.select_dtypes(include=np.number):
    df[col].fillna(df[col].median(), inplace=True)

for col in df.select_dtypes(include='object'):
    df[col].fillna("Unknown", inplace=True)

df.drop_duplicates(inplace=True)

# Filtering
filtered_df = df[df.select_dtypes(include=np.number).columns[0]]  # example safe line
print(filtered_df)

# Grouping example (change column names!)
# df.groupby('category')['sales'].mean()

print("Done")