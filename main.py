import pyautogui as pyauto
import pandas as pd
import json
from flask import Flask, jsonify, request
from time import sleep

def buy():
    pyauto.moveTo(-960, 780, duration=0.2)
    pyauto.click()
    pyauto.hotkey('shift', 'b')
    pyauto.sleep(0.3)
    pyauto.moveTo(-205, 615, duration=0.2)
    pyauto.click(duration=0.2)
    
def buydown():
    pyauto.moveTo(-960, 780, duration=0.2)
    pyauto.click()
    pyauto.hotkey('shift', 's')
    pyauto.sleep(0.3)
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

    if action == 'sell':
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

    return crrncapital, positions, downposition



def dataHandler(data):
    df = pd.DataFrame([data])
    with open('datafiles/money.json', 'r') as file:
        data = json.load(file)
    
    df.to_csv('data.csv', index=False, mode='a', header=False)
    crrncapital = data['capital']
    action = df.iloc[-1]['action']
    positions = data['positions']
    downposition = data['downposition']
    crrncapital, positions, downposition = trade(action, crrncapital, positions, downposition)
    
    data['capital'] = crrncapital
    data['positions'] = positions
    data['downposition'] = downposition
    
    with open('money.json', 'w') as file:
        json.dump(data, file)

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    if request.method == 'POST':
        data = request.json
        print('recived data: ',data)
        dataHandler(data)
        return jsonify({'status': 'success', 'message': 'Data received'}), 200
        
if __name__ == '__main__':
    app.run(host='192.168.0.193', port=80)
