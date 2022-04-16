import pandas as pd

df = pd.read_csv("books.csv", usecols=['ISBN'])
print(df)
df = df.drop_duplicates(subset=['ISBN'], keep="first", inplace=False)
print(df)