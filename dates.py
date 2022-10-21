import datetime
x = datetime.datetime.now()
y = datetime.datetime(2015, 10, 25)
print(x.year)
print(x.strftime("%A"))
print(y.strftime("%A"))