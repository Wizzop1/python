import pandas as pd
money = {'day one': 300,'day two': 250, 'day three': 200}
pd = pd.Series(money, index=['day one','day two'])
print(pd)