from mean import mean
data = [10,20,30,40,50,60]

def variance(data):
    #step 1:Find the mean for the data
    m = mean(data)
    sm = get_subtracted_mean(data,m)
    sq = square(sm)
    #step 4: Find the sum of the squares.
    sum_sq = sum(sq)
    #Step 5 : Divide the sum by N to get the variance.
    div = float(sum_sq / float(len(data)))
    return  div

#step 2: Subtract the mean from each data value.
def get_subtracted_mean(data,mean):
    return [i - mean for i in data]

#step 3:Square each result.
def square(data):
    return [i**2 for i in data]


print(variance(data))
