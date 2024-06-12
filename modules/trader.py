import pyautogui as pyauto
from time import sleep

class actions:
    def buy():
        pyauto.moveTo(-2780, 720, duration=0.2)
        pyauto.click()
        pyauto.hotkey('shift', 'b')
        sleep(0.3)
        pyauto.moveTo(-2150, 660, duration=0.2)
        pyauto.click(duration=0.2)
        
    def sell():
        pyauto.moveTo(-2780, 720, duration=0.2)
        pyauto.click()
        pyauto.hotkey('shift', 's')
        sleep(0.3)
        pyauto.moveTo(-2150, 660, duration=0.2)
        pyauto.click(duration=0.2)

def trade(action):
    if action == 'buy':
        actions.buy()
        
    elif action == 'sell':
        actions.sell()
            
    else:
        pass