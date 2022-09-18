# INF601 - Advanced Programming in Python
# James Kobell
# Test API call and print all data
import requests
import json
ticker = "TSLA"
params = {
    "access_key" : "key here",
    "symbols" : ticker}
api_get = "http://api.marketstack.com/v1/eod"
response = requests.get(api_get, params) #get call
if response.status_code == 200: #status code check
    print("\n\t",'{:*^60}'.format(f'EOD results for {ticker}')) # Title line for page
    print("\n")
    response_text = response.text
    response_json = json.loads(response_text) #convert to consumable json object
    for key in response_json['pagination']: # print key/value pairs in json object
        print("\t",key.title(), ':', response_json['pagination'][key], end ="  ");
    print("\n")
    for item in response_json['data']: # print array of json objects
        for key in item:
            print(key.title(), ':', item[key], end ="    ")
        print("\n")
else:
    print(f"\n\tAPI Call failed with status code {response.status_code}.") # error message if not status code 200