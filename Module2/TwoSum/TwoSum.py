'''
The goal of this problem is to implement a variant of the 2-SUM algorithm covered in this week's lectures.

input (given): array of numbers, homework file is not sorted but examples may be. 

Task: Target sum 't', can be any value but for the sake of this exercise we are looking for a range [-10000:10000]. Examples can be smaller in range.
Also to note, only care about there being a solution, not how many solutions per numbers.

'''
from multiprocessing import pool
import time


#~~~~~~~~~~~~~~~~~~~~~~~~~Test Cases~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
tc1 = [-3,-1,1,2,9,11,7,6,2] # output = 8
tc1_start = 3
tc1_end = 10

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

tc2 = [-2, 0, 0, 4] # output = 3
tc2_start = 0
tc2_end = 4

'''
walk through of tc2:
t = 0, 0 + 0
t = 1, no solution
t = 2, 4 +-2
t = 3, no solution
t = 4, 4 + 0
'''

tc3 = "Module2/TwoSum/input_random_10_40.txt" # output = 11
tc4 = "Module2/TwoSum/input_random_1_10.txt" # output = 2
tc5 = "Module2/TwoSum/input_random_18_160.txt" # output = 21
homeworkFile = "Module2/TwoSum/TwoSum.txt" # output correct based on soln below
h_start = -10000
h_end = 10000


#~~~~~~~~~~~~~~~~~~~~~~~~~~~Load File~~~~~~~~~~~~~~~~~~~~~~~~#
def loadData(filename):
    with open(filename, 'r') as file:
        a = list()
        for line in file:
            n = int(line)
            a.append(n)
    return a
            

#~~~~~~~~~~~~~~~~~~~~~~~~~~~Sort and Search routines~~~~~~~~~~~~~~~~~~~~~~~~#
def merge(left, right, result):
    i = j = 0
    while i + j < len(result):
        if j == len(right) or (i < len(left)) and left[i] < right[j]:
            result[i+j] = left[i]
            i += 1
        else:
            result[i+j] = right[j]
            j +=1

def mergeSort(seq):
    n = len(seq)
    if n < 2:
        return 

    mid = n//2
    lft = seq[0:mid]
    rgt = seq[mid:]

    mergeSort(lft)
    mergeSort(rgt)

    merge(lft, rgt, seq)
    return seq
    
def binarySearch(val, left, right, seq):
    
    if right >= left:
        mid = (left + right) // 2

        if val == seq[mid]:
            return True
        
        elif val < seq[mid]:
            return binarySearch(val, left, mid-1, seq)
        
        else:
            return binarySearch(val, mid+1, right, seq)
    
    else:
        return False

#~~~~~~~~~~~~~~~~~~~~~~~~~~~Tree/BinarySearchTree~~~~~~~~~~~~~~~~~~~~~~~~#


#~~~~~~~~~~~~~~~~~~~~~~~~~~~2SUM Routines~~~~~~~~~~~~~~~~~~~~~~~~#
def naive2SUM(data=None, file=None, start=None, end=None):
    '''
    Perform exhaustive search iterating through array combinations until solution found -> results in O(n^2)
    '''

    if file:
        data = loadData(file)

    sCount = 0

    while start <= end:
        i = 0
        while i < len(data):
            j = i+1
            while j < len(data):
                if data[i] + data[j] == start:
                    # solution exists
                    # print("target =", start)
                    # print(data[i], "+", data[j], "=", start)
                    sCount +=1
                    start +=1
                    i = 0
                    break
                if start > end:
                    return sCount
                j +=1
            i+=1
        start +=1
    return (sCount)


def sorted2SUM(data=None, file=None, start=None, end=None):
    '''
    1.) Sort input data up-front using O(n log(n)) method 
    2.) For each num in A, look-up target-num in A using binary search or another O(n log(n)) method
    '''

    solution = False
    sCount = 0

    # check which data to use, perform mergesort routine
    if data:
        data = mergeSort(data)
    elif file:
        data = loadData(file)
        data = mergeSort(data)

    # data is sorted, now perform target-num and binary search for matching result
    while (start <= end):    
        for num in data:
            val = start - num
            solution = binarySearch(val, 0, len(data)-1, data)
            if solution == True:
                sCount +=1
                break
        else:    
            start +=1

    return sCount

def hash2SUM(data=None, file=None, start=None, end=None):
    # check which data to use, perform mergesort routine

    h = dict()
    sCount = 0

    # load data + dictionary for searching
    if file:
        with open(file, 'r') as f:
            for line in f:
                num = int(line)
                h[num] = 1

    else:
        for num in data:
            h[num] = None

    while (start <= end):
        for num in h:
            val = start - num
            if val in h:
                sCount +=1
                start +=1
                break
        else:    
            start +=1

    return sCount
        
#~~~~~~~~~~~~~~~~~~~~~~~~~~~Main Program~~~~~~~~~~~~~~~~~~~~~~~~#
def main():
    print("RUNNING NAIVE SOLUTION")
    print("Number of solutions = ",naive2SUM(tc1,None,tc1_start,tc1_end))
    print("Number of solutions = ",naive2SUM(tc2,None,tc2_start,tc2_end))
    #print("Number of solutions = ",naive2SUM(None,homeworkFile,h_start,h_end))
    start = time.time()
    print("Number of solutions = ",naive2SUM(None,tc3,h_start,h_end))
    print("Elapsed time: ", time.time() - start)

    start = time.time()
    print("Number of solutions = ",naive2SUM(None,tc4,h_start,h_end))
    print("Elapsed time: ", time.time() - start)

    start = time.time()
    print("Number of solutions = ",naive2SUM(None,tc5,h_start,h_end))
    print("Elapsed time: ", time.time() - start)

    print("\nRUNNING SORTED SOLUTION")
    print("Number of solutions = ", sorted2SUM(tc1, None, tc1_start, tc1_end))
    print("Number of solutions = ", sorted2SUM(tc2, None, tc2_start, tc2_end))
    start = time.time()
    print("Number of solutions = ", sorted2SUM(None, tc3, h_start, h_end))
    print("Elapsed time: ", time.time()-start)

    start = time.time()
    print("Number of solutions = ", sorted2SUM(None, tc4, h_start, h_end))
    print("Elapsed time: ", time.time()-start)

    start = time.time()
    print("Number of solutions = ", sorted2SUM(None, tc5, h_start, h_end))
    print("Elapsed time: ", time.time()-start)

    start = time.time()
    print("Number of solutions = ", sorted2SUM(None, homeworkFile, h_start, h_end))
    print("Elapsed time: ", time.time()-start)

    print("\nRUNNING HASH SOLUTION")
    print("Number of solutions = ", hash2SUM(tc1, None, tc1_start, tc1_end))
    print("Number of solutions = ", hash2SUM(tc2, None, tc2_start, tc2_end))
    start = time.time()
    print("Number of solutions = ", hash2SUM(None, tc3, h_start, h_end))
    print("Elapsed time: ", time.time()-start)

    start = time.time()
    print("Number of solutions = ", hash2SUM(None, tc4, h_start, h_end))
    print("Elapsed time: ", time.time()-start)

    start = time.time()
    print("Number of solutions = ", hash2SUM(None, tc5, h_start, h_end))
    print("Elapsed time: ", time.time()-start)

    start = time.time()
    print("Number of solutions = ", hash2SUM(None, homeworkFile, h_start, h_end))
    print("Elapsed time: ", time.time()-start)

main()