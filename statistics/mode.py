from collections import Counter

z = [110, 731, 1031, 84, 20, 118, 1162, 1977, 103, 110]

def mode(data):
  data_dict = dict(Counter(z))
  return get_mode(data_dict)

def get_mode(dict):
  mode = 0
  topkey = 0
  #for counter, option in enumerate(options)
  for counter,key in enumerate(dict.keys()):
      if counter == 0 or dict[key] > mode :
        mode = dict[key]
        topkey = key
  return topkey
  
print(mode(z))
