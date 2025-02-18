import os
from dotenv import load_dotenv
import requests
import pprint
import json
from datetime import datetime



load_dotenv()

API_KEY=os.environ.get("API_KEY")
API_BASE_URL="https://holidayapi.com/"

#according to holidayapi.com documentation paramters should be in dictionary
parameters={
    "country" : "PK",
     "key" : API_KEY,
     "year": datetime.now().year-1


}
try: 
    response = requests.get(f"{API_BASE_URL}v1/holidays", params=parameters)
    response.raise_for_status()
except Exception:
    if response.status_code >= 400:
        print("Client error occured!")
    elif response.status_code >= 500:
        print("Server error please try again later!")
else:
    with open(r"C:\udemy\section_19\response.json", "w") as response_data:
        json.dump(response.json(), response_data, indent=4)