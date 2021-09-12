import csv
import numpy as np
import plotly.express as px

def getDatasrc(dataPath):
    Coffee=[]
    sleep=[]
    with open(dataPath) as csv_file:
        df = csv.DictReader(csv_file)
        for row in df:
            Coffee.append(float(row["Coffee"]))
            sleep.append(float(row["sleep"]))
    return{
        'x':Coffee,
        'y': sleep
    }

def findCorrelation(dataSource):
    correlation=np.corrcoef(dataSource['x'], dataSource['y'])
    print(correlation[0,1])

def setup():
    dataPath='data/cs.csv'
    dataSource=getDatasrc(dataPath)
    findCorrelation(dataSource)

setup()


    
