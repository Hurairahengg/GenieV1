import pandas as pd
import json
from time import sleep
from modules.webhook import EmailChecker as ec
from modules.trader import trade 

def dataHandler(data):
    newAction = None
    if data is not None:
        action = data.split()
        newAction = trade(action[0])
        return action
    else: 
        pass
    
    
    
    return newAction
    
while True:
    email_checker = ec()  
    data = email_checker.checkemail()  
    newAction = dataHandler(data)

    

