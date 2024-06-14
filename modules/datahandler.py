import json
from modules.trader import trade
from modules.logger import log

def dataHandler(data):
    if data is not None:
        cntpos = 0
        action = data.split()
        trade(action[0])
        time = log(action[0])

        cntpos = 1 if action[0] == 'buy' or action[0] == 'sell' else 0

        with open('data/position.json', 'r+') as pos:
            position_data = json.load(pos)
            position = position_data['positions']
            pos.seek(0)
            if action[0] == 'buy': json.dump({'positions': cntpos + position}, pos, indent=4)
            if action[0] == 'sell': json.dump({'positions': position - cntpos}, pos, indent=4)
            pos.truncate()
            
        return 'The trade for ' + action[0] + ' has been executed at ' + time
    else:
        pass
