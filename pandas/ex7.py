import pandas as pd
df = pd.read_csv('data2.csv')

df.fillna(200, inplace = True)

print(df.to_string())