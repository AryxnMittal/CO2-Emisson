import pandas as pd
import numpy as np

df = pd.read_csv("dataset.csv")

df = df.drop_duplicates()

for col in df.columns:
    if df[col].dtype == 'object':
        df[col].fillna(df[col].mode()[0], inplace=True)
    else:
        df[col].fillna(df[col].median(), inplace=True)

numeric_cols = df.select_dtypes(include=np.number).columns
for col in numeric_cols:
    mean = df[col].mean()
    std = df[col].std()
    df = df[(df[col] >= mean - 3*std) & (df[col] <= mean + 3*std)]

df.reset_index(drop=True, inplace=True)

df.to_csv("cleaned_data.csv", index=False)
