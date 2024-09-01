from modules.webhook import EmailChecker as ec
from modules.datahandler import dataHandler
from modules import start
import json
import pytz
import time 
import math
from datetime import datetime

jst = pytz.timezone('Asia/Tokyo')
timee = datetime.now(jst)
stop = timee.strftime('%H:%M') == "18:00" or timee.strftime('%A') == 'Friday' or timee.strftime('%A') == 'Saturday' or timee.strftime('%A') == 'Sunday'

def main():
    correct_password = "pgsp3007"
    password_attempts = 3

    for _ in range(password_attempts):
        password = start.getpass.getpass(prompt="Enter the password to proceed: ")
        if password == correct_password:
            print("Password accepted.")
            break
        else:
            print("Incorrect password. Try again.")
    else:
        print("Maximum password attempts exceeded. Exiting.S")
        return

    start.clear_screen()
    start.print_main_screen(first_time=True)
    start.init(text='Starting system')
    start.init(text="Checking internet connectivity")
    start.check_internet()
    print(' Done.')
    time.sleep(2)
    
    with open('data/position.json', 'r') as pos:
        data = json.load(pos)
        position = data.get('positions', None)
        
    with open('data/data.json', 'r') as file:
        data = json.load(file)
        position = data.get('positions', None)
        yesterdays_profit = data.get('lastpro', None)
        goal = data.get('goal', None)
        current_capital = data.get('currentcap', None)
        
    
    previous_position = position
    previous_current_capital = current_capital
    previous_yesterdays_profit = yesterdays_profit
    previous_goal = goal
    previous_market_status = "" 

    while True:
        email_checker = ec()
        data = email_checker.checkemail()
        logged = dataHandler(data)
        if logged:
            print(logged)
        
        with open('data/position.json', 'r') as pos:
            data = json.load(pos)
            position = data.get('positions', None)
            
        with open('data/data.json', 'r') as file:
            data = json.load(file)
            yesterdays_profit = data.get('lastpro', None)
            goal = data.get('goal', None)
            current_capital = data.get('currentcap', None)
        market_status = start.get_market_status_text()

        if (position != previous_position or 
            current_capital != previous_current_capital or 
            market_status != previous_market_status or
            yesterdays_profit != previous_yesterdays_profit or
            goal != previous_goal):
            
            start.clear_screen()
            start.print_main_screen(first_time=False)
            start.print_square_box(f"Trades Open: {position}",
                             f"Current Capital: ¥{current_capital}",
                             f"Today's Profit Goal: ¥500",
                             f"Units every trade: {1 if math.ceil(current_capital / 8000) == 2 else math.ceil(current_capital / 8000)}",
                             f"Yesterday Profit: ¥{yesterdays_profit}",
                             f"Money until goal: ¥{goal - yesterdays_profit}"
                             )
            start.print_market_status(market_status)
            previous_position = position
            previous_current_capital = current_capital
            previous_market_status = market_status
            previous_yesterdays_profit = yesterdays_profit
            previous_goal = goal


while True:
    main()