import requests
from getpass import getpass


auth_endpoint = "http://localhost:8000/api/auth/"
username = input("What is your username?\n")
password = getpass("What is your password?\n")
print(username, password)
auth_response = requests.post(auth_endpoint, json={'username': username, 'password': password})
print(auth_response.json())


if auth_response.status_code == 200:
    token = auth_response.json()['token']
    headers = {
        # "Authorization": f"Token {token}",
        "Authorization": f"Bearer {token}",
    }

    endpoint = "http://localhost:8000/api/products/4/update/"
    
    # data = {
    #     "title": "Hello world my old friend",
    #     "price": 125
    # }

    data = {
        "public": False,
        "title": "my old friend",
    }

    get_response = requests.put(endpoint, json=data, headers=headers)
    print(get_response.json())
