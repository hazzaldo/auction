# Auction

## Getting Started

To get a copy of the project code onto your local machine, run the command: 
```
git clone https://github.com/hazzaldo/auction.git
```

### Prerequisites
To avoid any incompatibility issues, please ensure you're on the Python version:
```
Python 3.8.2
```
Also refer to the `requirements.txt` file, located in the project root directory, for the list of required packages and their versions.

### Installing
Please ensure to create a Python virtual environment first to avoid installing packages globally that would potentially cause conflict.

Navigate to the project root directory, where you can see the `requirements.txt` file and run the command:
```
pip install -r requirements.txt
```

To run the Python program, navigate to the `src` folder, and run the command:
```
python main.py
```

This will create/output two log files to the `src` folder:

- `log_file.log` - which contains the output logs for all bids.

- `winning_bids_log_file.txt` - which contains the output logs for only the winning bids.
 
### Running the tests
The automated test are in the `test_app.py` file, in the project root directory. To run the tests, please ensure you're navigated to the project root directory and run the command:
```
pytest
```
Or the command below to output more information on the tests' result.
```
pytest -W ignore -s
```

### auction-test
This is to test the ability of solving problems in python. 

## The Task
You have been given auction data to process. Your program has to ingest the data and work out which account 
IDs win each auction and log them. The data is not in sequence meaning that you will get recieve the bids in random time order. There are some corrupt bid enteries which need to be filtered out and logged.

## Structure
The project takes the following structure:

```
├── README.md
├── src
│   ├── __init__.py
│   ├── data
│   │   ├── __init__.py
│   │   ├── bid.py
│   │   └── data.csv
│   └── main.py
```

The data handler is housed in the ```__init__.py``` file in the data directory. It loads the data from the 
CSV as soon as it's initialized. Use the ```.data``` property from the data handler to receive bid 
objects to process. You are free to add your own modules in the ```src``` directory and use them as you wish. The program should work by running the ```main.py``` file.  

## Restrictions 
Technically there's nothing stopping you from loading the CSV into pandas and performing data science 
methods to calculate the winner for each auction. However, it's important to demonstrate your problem 
solving skills when developing a system. Your program is supposed to handle the data as it comes in.
