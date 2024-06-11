import pyautogui as pyauto
from time import sleep

def buy():
    pyauto.moveTo(-960, 780, duration=0.2)
    pyauto.click()
    pyauto.hotkey('shift', 'b')
    sleep(0.3)
    pyauto.moveTo(-205, 615, duration=0.2)
    pyauto.click(duration=0.2)
    
def buydown():
    pyauto.moveTo(-960, 780, duration=0.2)
    pyauto.click()
    pyauto.hotkey('shift', 's')
    sleep(0.3)
    pyauto.moveTo(-205, 615, duration=0.2)
    pyauto.click(duration=0.2)

def trade(action, crrncapital, positions, downposition):
    if action == 'buy':
        if crrncapital >= 6000:
            if downposition == 0:
                buy()
                positions += 1
                crrncapital -= 6600
            elif downposition >= 1:
                buydown()
                sleep(0.5)
                crrncapital += 6600
                buy()
                positions += 1
                downposition = 0
                crrncapital -= 2300
        else:
            print('Not enough money :D')

    elif action == 'sell':
        if crrncapital >= 6000:
            if positions == 0:
                buydown()
                downposition += 1
                crrncapital -= 2300
            elif positions >= 1:
                buydown()
                sleep(0.3)
                crrncapital += 6600
                buydown()
                positions -= 1
                crrncapital -= 6600
        else:
            print('Not enough money :D')
            
    elif action == 'hold':
        pass

    return crrncapital, positions, downposition
