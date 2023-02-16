def minMax(t): # t must be iterable
    return min(t), max(t)

t = (4,45,-3,345)
r = minMax(t)
print(type(r))

