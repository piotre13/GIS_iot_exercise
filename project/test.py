import requests
response = requests.get('http://127.0.0.1:5001/earthquake_catalog')
print(response.json())