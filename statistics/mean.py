data = [20, 26, 40, 36, 23, 42, 35, 24, 30]

def sum(data):
  total = 0
  for n in data:
    total += n
  return total

def mean(data):
  total = sum(data)
  return total / len(data)
#x = sum(data)
print(mean(data))
