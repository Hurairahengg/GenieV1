import json
from modules.trader import trade
from modules.logger import log

def dataHandler(data):
    if data is not None:
        action = data.split()
        cntpos = 1 if action[0] in ['buy', 'sell'] else 0
        
        with open('data/position.json', 'r+') as pos:
            position_data = json.load(pos)
            position = position_data['positions']
            
            if action[0] == 'buy' and position < 1: 
                trade(action[0])
                position += cntpos
            elif action[0] == 'sell' and position > 0:
                trade(action[0])
                position -= cntpos
            
            pos.seek(0)
            json.dump({'positions': position}, pos, indent=4)
            pos.truncate()
            
            time = log(action[0])
            return 'The trade for ' + action[0] + ' has been executed at ' + time
    else:
        pass
