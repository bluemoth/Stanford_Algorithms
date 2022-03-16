'''
The goal of this problem is to implement the "Median Maintenance" algorithm (covered in the Week 3 lecture on heap applications).  
The text file contains a list of the integers from 1 to 10000 in unsorted order; you should treat this as a stream of numbers, arriving one by one.  
Letting Xi denote the ith number of the file, the kth median Mk is defined as the median of the numbers x1....xk.


Find the sum of these 10000 medians, modulo 10000 (i.e., only the last 4 digits). 

Important to handle all operations within O(log n) time (i.e heap operations)
Can easily incorporate a linear O(n) runtime routine to calculate median but avoid here

'''

import heapq
import time

# test files/cases
t0 = [1,3,3,6,7,8,9]
t1 = "Module2/MedianMaintenance/test1.txt" # 142
t2 = "Module2/MedianMaintenance/test2.txt" # 9335
t3 = "Module2/MedianMaintenance/test3.txt" # step by step procedure within forums, final sum = 717
t4 = "Module2/MedianMaintenance/input_random_10_40.txt" # 695
t5 = ""

homeworkFile = "Module2/MedianMaintenance/Median.txt" # numbers go from 1 to 100000, so median of this set is 5000. Split heaps based on this point

def median_maintenance_algorithm(filename):

    # holder for current calculated median val
    median_list = []
    runningSum = 0 
    heap_low = [] # will be a collection of negative numbers since heapq can only support min heap types/operations
    heap_high = [] # will be a normal collection of numbers
    low_Size = 0
    high_Size = 0

    # file loading
    with open(filename, 'r') as file:
        for line in file:
            # grab each number converting to int for processing...
            num = int(line)

            # first case, if heap_low is empty insert first element there
            if low_Size == 0:
                heapq.heappush(heap_low, -num)
                low_Size += 1
            elif low_Size > high_Size:
                if num >= -heap_low[0]:
                    # case of inbalance, check new median; if greater put in high
                    heapq.heappush(heap_high, num)
                else:
                    # is inbalanced, but new number needs to go low; transfer top value from low to high
                    heapq.heappush(heap_high, -(heapq.heappop(heap_low)))
                    heapq.heappush(heap_low, -num)
                high_Size += 1
            elif low_Size == high_Size:
                #no inbalance, can put in either
                if num > -heap_low[0]:
                    heapq.heappush(heap_low, -(heapq.heappop(heap_high)))
                    heapq.heappush(heap_high, num)
                else:
                    heapq.heappush(heap_low, -num)
                low_Size += 1

            
            

    print(heap_low, heap_high)

            


def main():
    start = time.time()

    median_maintenance_algorithm(t3)





    print("elapsed time: ", time.time() - start)

main()