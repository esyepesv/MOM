import requests
import time

url = 'http://localhost:5000/'

def client():

    while True:
        response = requests.get(url + "getRequest")
        if response.status_code == 200:
            print(response.json())
        time.sleep(2)
    
        

if __name__ == "__main__":
    client()
