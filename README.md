 ## INF601 - Advanced Programming in Python
 James Kobell |
 Mini Project 1

### Project
 Mini Project 1 is a Python project for retrieving and plotting the 'CLOSE' price during the 10 most recent trading days for 5 different ticker symbols. 

### Interpreter
Python 3.10.6

### Installation
- Create a directory for the project.
- Install Python 3.10.6 if not already installed.
- Refer to requirements.txt and pip install the listed packages.
- Update each package.
- Copy main.py into the directory.

### System Environment
- Within the directory of the project, create a directory with the name 'charts'.

### Running Project
- Obtain an access key from http://api.marketstack.com . 
- In main.py, replace the words, 'place key here' with a valid access key at `access_key = "place key here"`.
- From command line in the project directory or a suitable Python IDE, run main.py.
- Open the newly created 'charts' folder. Refer to the Environment section within this readme document.
- View each .png file with an application suitable for viewing .png files.
- To retrieve ticker data on a different set of ticker symbols, edit `tickers = ['AMZN', 'ETH', 'NCR', 'TSLA', 'XOM']` in main.py.

### Options
- To view each chart as they are created during the running of the project, uncomment `plt.show()` by removing the first '#' on the line.

### Alternate
#### ticker_data.py gets 100 days of data for a single ticker symbol
- Obtain an access key from http://api.marketstack.com . 
-  In ticker_data.py, replace the words, 'key here' with a valid access key at `"access_key" : "key here"`.
- Copy ticker_data.py into the directory.
- From command line in project directory or a suitable Python IDE, run ticker_data.py.
- View results displayed in the console window or terminal window.
- To retrieve ticker data on a different ticker symbol, edit `ticker = "TSLA"` in ticker_data.py. For example, replace 'TSLA' with a different symbol.

### Contributing
- Please open an issue to initiate a change process.

 

