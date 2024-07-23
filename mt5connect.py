import os

def write_trade_command(command):
    file_path = "/data/action.txt"
    with open(file_path, 'w') as file:
        file.write(f"[commands]\ntrade={command}\n")


write_trade_command("BUY") 
# write_trade_command("SELL")  
