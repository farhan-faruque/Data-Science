import json

#path ='../data/usagov_bitly_data2012-03-16-1331923249.txt'
#records = [json.loads(rec) for rec in open(path)]

def get_records(path = '../data/usagov_bitly_data2012-03-16-1331923249.txt'):
    return [json.loads(rec) for rec in open(path)]

#print(get_records()[0])