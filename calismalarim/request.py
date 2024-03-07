#GET REQUEST

import requests
import json

result = requests.get("https://jsonplaceholder.typicode.com/todos")
# print(result)  #Response [200]

result= json.loads(result.text) #json formatli tum sonuc type string


print(result[0]["title"])
print(result[0])
print(type(result))

for i in result:
    if i["userId"]==1:
       print(i["title"])   