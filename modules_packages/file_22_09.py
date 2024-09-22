import requests
from requests import Response

link: str = "https://pythonru.com/"

# https://docs-python.ru/packages/modul-requests-python/
response: Response = requests.get(link)
print(response.text)
