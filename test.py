import requests

model_inputs = {'code': open('code.py','r').read() }

res = requests.post('http://localhost:8000/', json=model_inputs)

print(res.json())
