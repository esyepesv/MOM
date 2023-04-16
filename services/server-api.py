import requests

url = 'http://localhost:5000/'

def client():

    while True:
        response = requests.get(url + "getRequest")
        if response.status_code == 200:
            print(response.json())

if __name__ == "__main__":
    client()
