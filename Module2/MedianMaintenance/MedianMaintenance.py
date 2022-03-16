'''
The goal of this problem is to implement the "Median Maintenance" algorithm (covered in the Week 3 lecture on heap applications).  
The text file contains a list of the integers from 1 to 10000 in unsorted order; you should treat this as a stream of numbers, arriving one by one.  
Letting Xi denote the ith number of the file, the kth median Mk is defined as the median of the numbers x1....xk.


Find the sum of these 10000 medians, modulo 10000 (i.e., only the last 4 digits). 
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
    heap_low = []
    heap_high = []
    low_Size = 0
    high_Size = 0

    # file loading
    with open(filename, 'r') as file:
        for line in file:
            # grab each number converting to int for processing
            num = int(line)

            # Grabbing items one-by-one
            if low_Size == 0:
                # Low heap empty, place first value in there. Update size, sum, and medians list for tracking
                heapq.heappush(heap_low, num)
                low_Size += 1
                runningSum += num
                median_list.append(num)
            
            # Check new incoming value against root heap_low
            
    
    print(heap_low, heap_high)

            


def main():
    start = time.time()

    median_maintenance_algorithm(t3)

    print("elapsed time: ", time.time() - start)

main()