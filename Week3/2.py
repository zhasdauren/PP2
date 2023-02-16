import sys

print(sys.getsizeof(tuple(iter(range(10)))))
print(sys.getsizeof(list(iter(range(10)))))

import timeit
print(timeit.timeit(stmt='[1,2,3,4,5,6,7,8,9,10]', number=1000000))
print(timeit.timeit(stmt='(1,2,3,4,5,6,7,8,9,10)', number=1000000))