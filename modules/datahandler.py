import json
from modules.trader import trade
from modules.logger import log
from datetime import datetime
from modules.sendMessage import send


def dataHandler(data):
    if data is not None:
        action = data.split()
        cntpos = 1 if action[0] in ['buy', 'sell'] else 0
        current_time = datetime.now().strftime("%d %H:%M")
        
        try:
            with open('data/position.json', 'r+') as pos:
                position_data = json.load(pos)
                position = position_data['positions']
            
                if action[0] == 'buy':
                    if position == 0:
                        trade(action[0])
                        position += cntpos
                        send(f'The {action[0]} trade has been executed at \n \n {current_time}')
                        log(action[0])

                    elif position < 0:
                        for x in range(abs(position)):
                            trade('buy')
                            position += cntpos
                        trade(action[0])
                        position += cntpos
                        send(f'The {action[0]} trade has been executed at \n {current_time}')
                        log(action[0])

                    elif position >= 1:
                        pass

                elif action[0] == 'sell':
                    if position == 0:
                        trade(action[0])
                        position -= cntpos
                        send(f'The {action[0]} trade has been executed at \n {current_time}')
                        log(action[0])

                    elif position > 0:
                        for x in range(position):
                            trade('sell')
                            position -= cntpos
                        trade(action[0])
                        position -= cntpos
                        send(f'The {action[0]} trade has been executed at \n {current_time}')
                        log(action[0])
                        
                    elif position <= -1:
                        pass
                if action[0] == 'bclose':
                    return 'Closing all positions...'

                pos.seek(0)
                json.dump({'positions': position}, pos, indent=4)
                pos.truncate()

                return f'The trade for {action[0]} has been executed at \n {current_time}'
        except Exception as e:
            print(f"An error occurred: {e}")
            return 'An error occurred while handling the data.'
    else:
        pass
