import json
from modules.webhook import EmailChecker as ec
from modules.datahandler import dataHandler

while True:
    email_checker = ec()
    data = email_checker.checkemail()
    logged = dataHandler(data)
    if logged:
        print(logged)
