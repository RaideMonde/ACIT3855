import requests

headers = { "Content-Type": "application/json" }

response = requests.post('http://localhost:8090/buy', headers=headers, data=json.dumps(event))
# or
response = requests.post('http://localhost:8090/buy', headers=headers, json=event)

return response.text, response.status_code
