# INF601 - Advanced Programming in Python
# James Kobell |
# Mini Project 1
import requests
import json
access_key = "place key here"
request_ticker = ""
response = ""
api_results = []
tickers = ['TSLA', 'NCR', 'ETH', 'AMZN', 'XOM']
api_get = "http://api.marketstack.com/v1/eod"
for ticker in tickers:
    request_ticker = ticker
    params = {
    "access_key" : access_key,
    "symbols" : request_ticker}
    response = requests.get(api_get, params) #get call
    api_results.append(response)
for result in api_results:
    if result.status_code == 200: #status code check
        response_text = result.text
        response_json = json.loads(response_text) #convert to consumable json object
        data = response_json['data']
        data_slice = data[0:10]
        print(data[0]['symbol'])
        for item in data_slice: # print list slice
            print(item['open'])
            print("\n")
    else:
        print(f"\n\tAPI Call failed with status code {result.status_code}.") # error message if not status code 200

