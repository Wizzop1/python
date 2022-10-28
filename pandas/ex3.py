import pandas as pd
fData = {
    'calories': [420, 70 , 230],
    'duration': [50,5,30]
}
varOne= pd.DataFrame(fData, index= ['day 1', 'day 2', 'day 3'])
print(varOne)
print(varOne.loc['day 3'])