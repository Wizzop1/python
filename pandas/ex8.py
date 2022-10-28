import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('data.csv')
print(df.corr())
df.plot(kind = "scatter", x = 'Duration', y = "Maxpulse")
plt.show()