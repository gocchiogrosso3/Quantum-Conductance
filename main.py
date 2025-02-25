import pandas as pd 
import numpy as np
import os

path = ''
files = [file for file in os.listdir(path) if os.path.isfile(os.path.join(path,file))]
for file in files:
    data = pd.read_table(os.path.join(path,file),index_col=None)
    time = np.array(data['Time'])
    voltage = np.array(data['Voltage'])
    #call other methods here 
