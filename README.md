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

To run the Python program, navigate to the project root directory folder, and run the command:
```
python main.py
```

This will create/output two log files to the project root directory:

- `log_file.log` - which contains the output logs for all bids.

- `winning_bids_log_file.txt` - which contains the output logs for only the winning bids.
 
### Running the tests
The automated test are in the `test_app.py` file, in the project root directory. To run the tests, please ensure you're in the project root directory and run the command:
```
pytest
```
Or the command below to output more information on the tests' result.
```
pytest -W ignore -s
```

### auction-test
This is to test the ability of solving problems in python. 

## Functionality
Given auction data to process, the program ingests the data and works out which account IDs win each auction and log them. The data is not in sequence - meaning the program can receive the bids in random time order and still be able to process them. Also there are some corrupt bid entries which the program can still filter out and log.

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

The data handler is housed in the ```__init__.py``` file in the data directory. It loads the data from the CSV as soon as it's initialized. The ```.data``` property from the data handler is used to receive bid 
objects to process. The program is launched by running the ```main.py``` file.  

Technically there's nothing stopping someone from loading the CSV into pandas and performing data science methods to calculate the winner for each auction. However, this program demonstrates problem 
solving skills when developing a system. The program is supposed to handle the data as it comes in.
