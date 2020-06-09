# auction-test
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
