import requests

response = requests.get(
    "https://api.chucknorris.io/jokes/random",
    headers={
        "Content-Type": "application/json",
    },
)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print("Error: ", response.status_code)
