import pandas as pd
dataset = {
    'cars':['Volvo','BMW',"Ford"],
    'passings':[3,4,7]
}
f_var = pd.DataFrame(dataset)
dataset2 = {
    'phones':['Samsung','Huawei','Iphone'],
    'RAM':[8,8,3]
}
t_var = pd.Series(dataset2, index = ['ph','ram'])
#print(f_var)
#print(pd.__version__)
