data = [2, 3, 6, 8, 4, 1]
def mid_range(data):
  if len(data)  == 0:
    return 0
  elif len(data) == 1:
    return data[0]
  else:
    sum = min(data) + max(data)
    return sum / 2
print(mid_range(data))
