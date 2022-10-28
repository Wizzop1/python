import pandas as pd
df = pd.read_csv('data.csv')
#print(df.to_string())
print(df.head(10))
print(df.tail(10))
print(df.info())