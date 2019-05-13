import time
import os
import csv
import ipywidgets as widgets

def generateFileName():
    return '_'.join(time.ctime().split()[1:-1]) + '.csv'

def readAndSave(list_response):
    filename = generateFileName()
    if 'data' not in os.listdir('.'):
        print('####Build up the data folder####')
        os.system('mkdir data')
    
    with open(os.path.join('data', filename), 'w') as f:
        for key in list_response.keys():
            f.write("%s,%s\n"%(key,str(list_response[key])))