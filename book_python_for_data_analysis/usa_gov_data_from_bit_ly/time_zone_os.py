__author__ = 'farhan'

from pandas import DataFrame,Series
import pandas as pd
import numpy as np
import gov_data_fetcher
import matplotlib.pyplot as plt

records = gov_data_fetcher.fetch_records()
frame = DataFrame(records)
results = Series([x.split()[0] for x in frame.a.dropna()])
cframe = frame[frame.a.notnull()]
operating_system = np.where(cframe['a'].str.contains('Windows'),'Windows','Not Windows')
by_tz_os = cframe.groupby(['tz',operating_system])
agg_counts = by_tz_os.size().unstack().fillna(0)
indexer = agg_counts.sum(1).argsort()
count_subset = agg_counts.take(indexer)[-10:]
#count_subset.plot(kind='barh', stacked=True)
normed_subset = count_subset.div(count_subset.sum(1),axis = 0)
normed_subset.plot(kind='barh', stacked=True)
plt.show()
#print(count_subset)