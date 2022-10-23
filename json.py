from json import loads
x= '{"name": "George", "age": "20", "city": "Sofia"}' 
y = json.loads(x)
print(y["city"])