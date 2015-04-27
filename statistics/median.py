
data = [209, 223, 211, 227, 213, 240, 240, 211, 229, 212]
def median(data):
    data.sort()
    middle = int(mid(len(data)))
    if is_even(len(data)):
      average = avg(data[middle - 1],data[middle])
    else:
      average = data[middle]
    return average

def is_even(number):
  return number % 2 == 0

def mid(number):
  return number / 2

def avg(*numbers):
    total = 0.0;
    for n in numbers:
      total += n;
    return int(total / len(numbers))

print(median(data))
