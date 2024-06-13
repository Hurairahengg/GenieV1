import json
from trader import trade
from logger import log


def dataHandler(data):
    if data is not None:
        with open('data/position.json', 'w') as pos:
            json.dump({'positions': cntpos}, pos, indent=4)

        action = data.split()
        if pos < 1:
            trade(action[0])
        time = log(action[0])

        cntpos = 1 if action[0] == 'buy' else - \
            1 if action[0] == 'sell' else cntpos

        return 'The trade for ' + action[0] + ' has been executed at ' + time
    else:
        pass
