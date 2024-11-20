import requests

def fetch_objects():
    url = "https://api.restful-api.dev/objects"

    try:
        response = requests.get(url)
        response.raise_for_status()
        objects = response.json()
        for obj in objects:
            print(obj)
       
    except requests.exceptions.RequestException as e:
        print(f"An Error occurred: {e}")

if __name__ == "__main__":
    fetch_objects()