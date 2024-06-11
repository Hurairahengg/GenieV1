import pandas as pd
import json
from time import sleep
from modules.webhook import EmailChecker as ec
from modules.trader import trade 

def dataHandler(data):
    data = rawData.split()
    action = data[0]
    
    crrncapital, positions, downposition = trade(action, crrncapital, positions, downposition)
    
while True:
    email_checker = ec()  # Create an instance of EmailChecker
    rawData = email_checker.checkemail()  # Call the method on the instance
    dataHandler(rawData)

