# INF601 - Advanced Programming in Python
# James Kobell |
# Mini Project 1
import requests
import json
import numpy as np # import numpy
import matplotlib.pyplot as plt # import matplotlib.pyplot
import dateparser as dp # for parse json datetime string value
access_key = "place key here" # DO NOT show in commits; todo: get from file
request_ticker = ""
response = ""
api_results = [] # declare list of responses for each api call
#tickers = ['TSLA', 'NCR', 'ETH', 'AMZN', 'XOM'] # todo get from input control
tickers = ['AMZN', 'ETH', 'NCR', 'TSLA', 'XOM'] # todo get from input control
api_get = "http://api.marketstack.com/v1/eod" # todo: get from file
for ticker in tickers: # loop through ticker list
    request_ticker = ticker
    params = {
    "access_key" : access_key,
    "symbols" : request_ticker}
    response = requests.get(api_get, params) #get call; todo: wrap in try except; log except
    api_results.append(response) 
for result in api_results:
    if result.status_code == 200: #status code check
        response_text = result.text
        response_json = json.loads(response_text) #convert to consumable json object
        data = response_json['data']
        data_slice = data[0:10]  # slice of first ten
        data_closeprice = [] # declare list
        labels = [] # declare list for xtick      
        for item in data_slice: 
            time = dp.parse(item['date']) # convert value to datetime object
            ftime = time.strftime("%m/%d/%Y") # format date
            labels.append(ftime)            
            data_closeprice.append(item['close'])
        closeprice_nparray = np.array(data_closeprice) # convert data list to numpy array
        tickername = item['symbol']
        plt.figure() # must create figure object to prevent summation -- race condition?
        plt.plot(closeprice_nparray) # move all plt.xxxx to a method
        plt.gca().invert_xaxis() # reverse x axis
        plt.ylabel('Close price')
        plt.title(tickername)
        plt.xticks(np.arange(10), labels, rotation = 30)        
        plt.margins(.05, .1) # padding
        plt.tight_layout()
        plt.savefig(f"charts/{tickername}.png", facecolor = "#cfd9e4") # todo: wrap in try except, log except
        # plt.show() # uncomment to show
    else: 
        print(f"\n\tAPI Call failed with status code {result.status_code}.") # error message if not status code 200

