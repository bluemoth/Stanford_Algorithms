'''
The goal of this problem is to implement a variant of the 2-SUM algorithm covered in this week's lectures.

input (given): array of numbers, homework file is not sorted but examples may be. 

Task: Target sum 't', can be any value but for the sake of this exercise we are looking for a range [-10000:10000]. Examples can be smaller in range.
Also to note, only care about there being a solution, not how many solutions per numbers.

'''


import time

tc1 = [-3,-1,1,2,9,11,7,6,2] # target sum is :[3,10], (i.e 3, 4, 5, 6, 7, 8, 9, 10) output = 8
''' 
Walk through of tc1:
t = 3, 6 + -3
t = 4, 7 + -3
t = 5, 6 + -1 
t = 6, 7 + -1
t = 7, 6 + 1
t = 8, 6 + 2
t = 9, 7 + 2
t = 10, 11 +- 1
'''

tc2 = [-2, 0, 0, 4] # t[0:4], output = 3
'''
walk through of tc2:
t = 0, 0 + 0
t = 1, no solution
t = 2, 4 +-2
t = 3, no solution
t = 4, 4 + 0
'''

homeworkFile = "Stanford_Algorithms/Module2/TwoSum/TwoSum.txt"


def loadData(filename):
    print(filename)



def naive2SUM():
    print("naive")


def sort2SUM():
    print("sort")


def hash2SUM():
    print("hash")



def main():
    loadData(homeworkFile)

main