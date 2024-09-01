import os
from time import sleep
import requests
import getpass
import shutil
import pandas_market_calendars as mcal
import json
from datetime import datetime, timedelta

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def init(text):
    print("\n", text, end="", flush=True)
    for i in range(3):

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
        os.exit(0)

def print_main_screen(first_time=True):
    if first_time:
        clear_screen()
        lines = [
            "                                                                                                                               "
            "                                                                                                                               ",
            "            ||||||||||| ||||||||||    |||     ||   ||||    || |||||||||||       |||     |||     |||          |||        |||||||",
            "               |+|         |+|      |+|+|   |+|  |+|+|   |+|     |+|           |+|     |+|   |+|+|        |+|+|       |+|   |+|",
            "              +|+         +|+      |+|+|+  +|+  |+|+|+  +|+     +|+           +|+     +|+     +|+          +|+       +|+   +|+",
            "             +#+         +#+      +#+ +|+ +#+  +#+ +|+ +#+     +#+           +#+     +|+     +#+          +#+       +#+   +|+",
            "            +#+         +#+      +#+  +#+#+#  +#+  +#+#+#     +#+            +#+   +#+      +#+          +#+       +#+   +#+",
            "      +#   +#+         #+#      #+#   #+#+#  #+#   #+#+#     #+#             #+#+#+#       #+#   #+#    #+#   #+# #+#   #+#",
            "     #######     ###########  ###    ####  ###    #### ###########           ###     ######### ###  ####### ###  #######"
        ]
        for line in lines:
            print(line)
            sleep(0.035)
    else:
        clear_screen()
        print("""
            ||||||||||| ||||||||||    |||     ||   ||||    || |||||||||||      |||     |||     |||          |||         |||||||"
               |+|         |+|      |+|+|   |+|  |+|+|   |+|     |+|          |+|     |+|   |+|+|        |+|+|       |+|   |+|"
              +|+         +|+      |+|+|+  +|+  |+|+|+  +|+     +|+          +|+     +|+     +|+          +|+       +|+   +|+"
             +#+         +#+      +#+ +|+ +#+  +#+ +|+ +#+     +#+          +#+     +|+     +#+          +#+       +#+   +|+"
            +#+         +#+      +#+  +#+#+#  +#+  +#+#+#     +#+           +#+   +#+      +#+          +#+       +#+   +#+"
      +#   +#+         #+#      #+#   #+#+#  #+#   #+#+#     #+#            #+#+#+#       #+#   #+#    #+#   #+# #+#   #+#"
     #######     ###########  ###    ####  ###    #### ###########          ###       ####### ###  ####### ###  #######"
        """)

def get_market_status(market_calendar, name):
    now = datetime.now()
    schedule = market_calendar.schedule(start_date=now.date(), end_date=now.date() + timedelta(days=1))
    if schedule.empty:
        return f"{name}: Closed"
    market_open = schedule.iloc[0]['market_open'].to_pydatetime().replace(tzinfo=None)
    market_close = schedule.iloc[0]['market_close'].to_pydatetime().replace(tzinfo=None)
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

def print_square_box(text1, text2, text3, text4, text5, text6):
    box_width = 30
    terminal_size = shutil.get_terminal_size((80, 20))
    screen_width = terminal_size.columns
    left_padding = (screen_width - box_width) // 2

    print(f"{' ' * left_padding}+{'-' * (box_width - 2)}+")
    print(f"{' ' * left_padding}| {text1:<{box_width - 4}} |")
    print(f"{' ' * left_padding}| {text2:<{box_width - 4}} |")
    print(f"{' ' * left_padding}| {text3:<{box_width - 4}} |")
    print(f"{' ' * left_padding}| {text4:<{box_width - 4}} |")
    print(f"{' ' * left_padding}| {text5:<{box_width - 4}} |")
    print(f"{' ' * left_padding}| {text6:<{box_width - 4}} |")
    print(f"{' ' * left_padding}+{'-' * (box_width - 2)}+")

