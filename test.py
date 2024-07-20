import os
from time import sleep
import requests
import getpass
import shutil
import pandas_market_calendars as mcal
from datetime import datetime, timedelta

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def init(text):
    print("\n", text, end="", flush=True)
    for i in range(3):
        sleep(1)
        print(".", end="", flush=True)
    print()

def check_internet():
    url = "http://www.google.com"
    timeout = 5
    try:
        _ = requests.get(url, timeout=timeout)
        print("\n Connected to the Internet \n")
    except requests.ConnectionError:
        print("No internet connection")

def print_main_screen(first_time=True):
    if first_time:
        clear_screen()
        sleep(1)
        lines = [
            "                                                                                                                               ",
            "            ||||||||||| ||||||||||    |||     ||   ||||    || |||||||||||       |||     |||  ||||||||        |||        |||||||",
            "               |+|         |+|      |+|+|   |+|  |+|+|   |+|     |+|           |+|     |+| |+|    |+|     |+|+|       |+|   |+|",
            "              +|+         +|+      |+|+|+  +|+  |+|+|+  +|+     +|+           +|+     +|+       +|+        +|+       +|+   +|+",
            "             +#+         +#+      +#+ +|+ +#+  +#+ +|+ +#+     +#+           +#+     +|+     +#+          +#+       +#+   +|+",
            "            +#+         +#+      +#+  +#+#+#  +#+  +#+#+#     +#+            +#+   +#+    +#+            +#+       +#+   +#+",
            "      +#   +#+         #+#      #+#   #+#+#  #+#   #+#+#     #+#             #+#+#+#    #+#       #+#   #+#   #+# #+#   #+#",
            "     #######     ###########  ###    ####  ###    #### ###########           ###     ########## ### ####### ###  #######"
        ]
        for line in lines:
            print(line)
            sleep(0.085)
    else:
        clear_screen()
        print("""
            ||||||||||| ||||||||||    |||     ||   ||||    || |||||||||||       |||     |||  ||||||||        |||        |||||||
               |+|         |+|      |+|+|   |+|  |+|+|   |+|     |+|           |+|     |+| |+|    |+|     |+|+|       |+|   |+|
              +|+         +|+      |+|+|+  +|+  |+|+|+  +|+     +|+           +|+     +|+       +|+        +|+       +|+   +|+
             +#+         +#+      +#+ +|+ +#+  +#+ +|+ +#+     +#+           +#+     +|+     +#+          +#+       +#+   +|+
            +#+         +#+      +#+  +#+#+#  +#+  +#+#+#     +#+            +#+   +#+    +#+            +#+       +#+   +#+
      +#   +#+         #+#      #+#   #+#+#  #+#   #+#+#     #+#             #+#+#+#    #+#       #+#   #+#   #+# #+#   #+#
     #######     ###########  ###    ####  ###    #### ###########           ###     ########## ### ####### ###  #######
        """)

def get_market_status(market_calendar, name):
    now = datetime.now()
    schedule = market_calendar.schedule(start_date=now.date(), end_date=now.date() + timedelta(days=1))
    if schedule.empty:
        return f"{name}: Closed"
    market_open = schedule.iloc[0]['market_open']
    market_close = schedule.iloc[0]['market_close']
    if market_open <= now <= market_close:
        return f"{name}: Open"
    else:
        return f"{name}: Closed"

def get_market_status_text():
    nyse = mcal.get_calendar('NYSE')
    lse = mcal.get_calendar('LSE')
    tyo = mcal.get_calendar('JPX')
    asx = mcal.get_calendar('ASX')
    nyse_status = get_market_status(nyse, "NYC")
    lse_status = get_market_status(lse, "London")
    tyo_status = get_market_status(tyo, "Tokyo")
    asx_status = get_market_status(asx, "Sydney")
    status_text = f"{nyse_status} | {lse_status} | {tyo_status} | {asx_status}"
    return status_text

def print_market_status(status_text):
    terminal_size = shutil.get_terminal_size((80, 20))
    screen_width = terminal_size.columns
    left_padding = (screen_width - len(status_text)) // 2
    print(f"{' ' * left_padding}{status_text}")

def print_square_box(trades_open, starting_capital, current_capital, today_profit):
    box_width = 30
    text1 = f"Trades Open: {trades_open}"
    text2 = f"Starting Capital: ${starting_capital}"
    text3 = f"Current Capital: ${current_capital}"
    text4 = f"Today Profit: ${today_profit}"
    terminal_size = shutil.get_terminal_size((80, 20))
    screen_width = terminal_size.columns
    left_padding = (screen_width - box_width) // 2
    print(f"{' ' * left_padding}+{'-' * (box_width - 2)}+")
    print(f"{' ' * left_padding}| {text1:<{box_width - 4}} |")
    print(f"{' ' * left_padding}| {text2:<{box_width - 4}} |")
    print(f"{' ' * left_padding}| {text3:<{box_width - 4}} |")
    print(f"{' ' * left_padding}| {text4:<{box_width - 4}} |")
    print(f"{' ' * left_padding}+{'-' * (box_width - 2)}+")

def main():
    correct_password = "pgsp3007"
    password_attempts = 3

    for _ in range(password_attempts):
        password = getpass.getpass(prompt="Enter the password to proceed: ")
        if password == correct_password:
            print("Password accepted.")
            break
        else:
            print("Incorrect password. Try again.")
    else:
        print("Maximum password attempts exceeded. Exiting.")
        return

    clear_screen()
    print_main_screen(first_time=True)
    init(text='Starting system')
    init(text="Checking internet connectivity")
    check_internet()
    print(' Done.')
    sleep(3)
    trades_open = 0
    starting_capital = 10000
    current_capital = 10000
    today_profit = 0
    previous_trades_open = trades_open
    previous_current_capital = current_capital
    previous_today_profit = today_profit
    previous_market_status = ""

    while True:
        trades_open += 1
        current_capital += 50
        today_profit += 50
        market_status = get_market_status_text()

        if (trades_open != previous_trades_open or 
            current_capital != previous_current_capital or 
            today_profit != previous_today_profit or 
            market_status != previous_market_status):
            
            clear_screen()
            print_main_screen(first_time=False)
            print_square_box(trades_open, starting_capital, current_capital, today_profit)
            print_market_status(market_status)
            previous_trades_open = trades_open
            previous_current_capital = current_capital
            previous_today_profit = today_profit
            previous_market_status = market_status

        sleep(1)

if __name__ == "__main__":
    main()
