import gov_data_fetcher
from collections import defaultdict
from collections import Counter

records = gov_data_fetcher.fetch_records()
time_zones = [rec['tz'] for rec in records if 'tz' in rec]

def get_counts(sequence):
    counts = {}
    for x in sequence:
        if x in counts:
            counts[x] += 1
        else:
            counts[x] = 1
    return counts

def get_counts2(sequence):
    counts = defaultdict(int)
    for x in sequence:
        counts[x] += 1
    return counts

def top_counts(count_dict, n = 10):
    value_key_pairs = [(count, tz) for tz, count in count_dict.items()]
    value_key_pairs.sort()
    return value_key_pairs[-n:]

def top_counts2(time_zones,n = 10):
    counts = Counter(time_zones)
    return counts.most_common(n)

#counts = get_counts2(time_zones)
print(top_counts2(time_zones))