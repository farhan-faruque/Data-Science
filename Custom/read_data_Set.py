import pandas as pd
from pandas import DataFrame,Series

# def mask(df,key,value):
#     return  df[df[key] == value]

def mask(df,f):
    return df[f(df)]

unames = ['name', 'mfr',  'type', 'calories', 'protein', 'fat', 'sodium', 'fiber', 'carbo', 'sugars', 'shelf', 'potass', 'vitamins', 'weight', 'cups']
cereal = pd.read_table( 'data/cereal.txt', names = unames, sep = ' ')
df = DataFrame(cereal)
l = lambda x: x.fat < 1
val = mask(df,l)
print(val)