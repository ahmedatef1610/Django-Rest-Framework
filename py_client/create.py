import requests


headers = {'Authorization': 'Bearer faaba59680f165b2c8f6c036c05758b65bfda6d6'}
endpoint = "http://localhost:8000/api/products/"

data = {
    "title": "This field is done",
    "price": 32.99
}

# get_response = requests.post(endpoint, json=data)
get_response = requests.post(endpoint, json=data, headers=headers)
print(get_response.json())
