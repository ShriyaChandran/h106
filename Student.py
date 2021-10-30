import csv
import numpy as np
import plotly.express as px

def getDatasrc(dataPath):
    Marks=[]
    Days=[]
    with open(dataPath) as csv_file:
        df = csv.DictReader(csv_file)
        for row in df:
            Marks.append(float(row["Marks"]))
            Days.append(float(row["Days"]))
    return{
        'x':Marks,
        'y': Days
    }

def findCorrelation(dataSource):
    correlation=np.corrcoef(dataSource['x'], dataSource['y'])
    print(correlation[0,1])

def setup():
    dataPath='data/Student.csv'
    dataSource=getDatasrc(dataPath)
    findCorrelation(dataSource)

setup()


    
