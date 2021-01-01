import requests,json
from pprint import pprint

def get_url_data(url):
    r = requests.get(url)
    return r.json()

def get_file_data(file):
    with open(file) as f:
        data = json.load(f)
    return data