import requests
import pprint

API_BASE_URL="https://restcountries.com"
response=requests.get(f"{API_BASE_URL}/v3.1/all?feilds=name,flags")
json_data=response.json()
pprint.pprint(json_data)
