from pandas import DataFrame,Series
import pandas as pd
import gov_data_fetcher
import matplotlib.pyplot as plt

records = gov_data_fetcher.fetch_records()
time_zones = [rec['tz'] for rec in records if 'tz' in rec]
frame = DataFrame(records)
#time_zones_counts = frame['tz'].value_counts()
clean_tz = frame['tz'].fillna('Missing')
clean_tz[clean_tz == ''] = 'Unknown'
tz_counts = clean_tz.value_counts()
#print(tz_counts[:10])
tz_counts[:10].plot(kind='barh', rot=0)
plt.show()