import os
from dotenv import load_dotenv
import requests
import pprint
import json
from datetime import datetime



load_dotenv()

API_KEY=os.environ.get("API_KEY")
API_BASE_URL="https://holidayapi.com/"

#accroding to holidayapi.com documentation paramters should be in dictionary
parameters={
    "country" : "PK",
     "key" : API_KEY,
     "year": datetime.now().year-1 # bcoz in free api no current data is present only historic data


}



response=requests.get(f"{API_BASE_URL}/v1/holidays",params=parameters)
json_data = response.json()
pprint.pprint(json_data)



