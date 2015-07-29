__author__ = 'farhan'
import pandas as pd

years  = range(1880,2014)
pieces = []
columns = ['name','sex','births']

for year in years:
    path = '../data/names/yob%d.txt' %year
    frame = pd.read_csv(path,names = columns)

    frame['year'] = year
    pieces.append(frame)

names = pd.concat(pieces,ignore_index=True)
print(names)
