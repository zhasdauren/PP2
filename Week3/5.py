'''
1) Write a Python program to extract 
year, month, date and time using Lambda.
Sample Output:
2020-01-15 09:03:32
2020
1
15
09:03:32
'''
def extract(s):
    x = lambda s: s.split()
    y = lambda s: s.split('-')
    t = y(x(s)[0])
    print(t[0])
    print(t[1])
    print(t[2])


s = input()
print(extract(s))

'''
2) Write a Python program to count the even and odd numbers in a given array of integers using Lambda.
Original arrays:
[1, 2, 3, 5, 7, 8, 9, 10]
Number of even numbers in the above array: 3
Number of odd numbers in the above array: 5
'''
