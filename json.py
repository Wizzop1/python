from json import loads
import json
x= '{"name": "George", "age": "20", "city": "Sofia"}' 
y = json.loads(x)
print(y["city"])