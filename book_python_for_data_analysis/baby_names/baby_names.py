__author__ = 'farhan'
import pandas as pd

names1880 = pd.read_csv('../data/names/yob1880.txt', names = ['name', 'sex', 'births'])
#names1880.group_by('sex')
print(names1880.groupby('sex').births.sum())