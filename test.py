import os
from time import sleep
import requests
os.system('cls')


def init(text):
    print("\n", text , end="", flush=True)
    for i in range(3):
        sleep(1)
        print(".", end="", flush=True)
def check_internet():
    
    url = "http://www.google.com"
    timeout = 5
    try:
        _ = requests.get(url, timeout=timeout)
        print("\n Connected to the Internet")
    except requests.ConnectionError:
        print("No internet connection")

sleep(1)
print("""                                                                                                                          """)
print("""                                                                                                                          """)
print("""                                                                                                                          """)
print("""        ||||||||||| ||||||||||    |||     ||   ||||    || |||||||||||       |||     |||  ||||||||        |||        |||||||""")
sleep(0.035)
print("           |+|         |+|      |+|+|   |+|  |+|+|   |+|     |+|           |+|     |+| |+|    |+|     |+|+|       |+|   |+|")
sleep(0.035)
print("          +|+         +|+      |+|+|+  +|+  |+|+|+  +|+     +|+           +|+     +|+       +|+        +|+       +|+   +|+")
sleep(0.025)
print("         +#+         +#+      +#+ +|+ +#+  +#+ +|+ +#+     +#+           +#+     +|+     +#+          +#+       +#+   +|+")
sleep(0.025)
print("        +#+         +#+      +#+  +#+#+#  +#+  +#+#+#     +#+            +#+   +#+    +#+            +#+       +#+   +#+")
sleep(0.015)
print("  +#   +#+         #+#      #+#   #+#+#  #+#   #+#+#     #+#             #+#+#+#    #+#       #+#   #+#   #+# #+#   #+#")
sleep(0.015)
print(" #######     ###########  ###    ####  ###    #### ###########           ###     ########## ### ####### ###  #######")

init(text='Starting system')
init(text="Checking internet connectivity")
check_internet()
