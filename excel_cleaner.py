import pandas as pd

df = pd.read_excel("input.xlsx")
df = df.dropna()
df = df.drop_duplicates()
df.to_excel("cleaned_output.xlsx", index=False)

print("Excel cleaned successfully")
