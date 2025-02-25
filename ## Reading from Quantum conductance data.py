## Reading from Quantum conductance data 

from matplotlib import pyplot as plt
import numpy as np
import pandas as pd


input_file = QC_data.txt
txt_file = QC_Clean_data.txt

rtimes = [] #lists for now will put in numpy later (still deciding how to seperate runs)
rVoltages = []


## This code will only read first run 
with open(txt_file,'w+') as txt:
    # Read the input file
    with open(input_file, 'r') as file:
        #parse through input file
        for line in file:
            if line[1] == 'R':
                rec_time, recV = line.split('^') #split each line by the ^ symbol 
                t = rec_time[12:-1] #record just the number
                p = recV[15:-1] #record just the voltage
                rtimes.append(t) #add to times list
                rVoltages.append(p) #add to voltages list 
                #txt.write(p + '\n')
            if line[1] != 'R':
                break

                