
import os
import pandas as pd

class Logger:
    '''logs chat data to csv file'''
    def __init__(self, channel):
        self.channel = channel
        self.data = []

    def write_to_file(self):
        csv_data = pd.DataFrame().from_records(self.data)
        filename = f'../logs/{self.channel}.csv'

        if os.path.isfile(filename):
            csv_data.to_csv(filename, mode='a', header=False, index=False)
        else:
            csv_data.to_csv(filename, sep='\t', index=False)



