import pandas as pd
from datetime import datetime


def log(action):
    time = datetime.now().strftime("%d %H:%M")
    data = {
        'action': [action],
        'time': [datetime.now().strftime("%Y-%m-%d %H:%M")]
    }

    df = pd.DataFrame(data)
    df.to_csv('data/data.csv', index=False, mode='a',
              header=not pd.io.common.file_exists('data.csv'))
    return time
