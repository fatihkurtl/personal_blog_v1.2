import requests
import json

url = 'http://127.0.0.1:5000/api/register'

data = {
    'email': 'kurtf061@gmail.com',
    'password': '123456'
}

headers = {'Content-Type': 'application/json'}

response = requests.post(url, data=json.dumps(data), headers=headers)

