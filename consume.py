from urllib import response
import requests

response = requests.get('http://127.0.0.1:8000/drinks.json')
print(response.json())

#print("testing")
