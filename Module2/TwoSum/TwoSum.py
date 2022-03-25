'''
The goal of this problem is to implement a variant of the 2-SUM algorithm covered in this week's lectures.

input (given): array of numbers, homework file is not sorted but examples may be. 

Task: Target sum 't', can be any value but for the sake of this exercise we are looking for a range [-10000:10000]. Examples can be smaller in range.
Also to note, only care about there being a solution, not how many solutions per numbers.

'''
import time


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

homeworkFile = "Module2/TwoSum/TwoSum.txt"
h_start = -10000
h_end = 10000



def loadData(filename):
    with open(filename, 'r') as file:
        a = list()
        for line in file:
            n = int(line)
            a.append(n)
    return a
            

def naive2SUM(data=None, file=None, start=None, end=None):
    # quadratic, naive solution cycling through all possibilities to find solutions

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
    


def main():
    print("Number of solutions = ",naive2SUM(tc1,None,tc1_start,tc1_end))
    print("Number of solutions = ",naive2SUM(tc2,None,tc2_start,tc2_end))
    #print("Number of solutions = ",naive2SUM(None,homeworkFile,h_start,h_end))
    start = time.time()
    print("Number of solutions = ",naive2SUM(None,tc3,h_start,h_end))
    print("Elapsed time: ", time.time() - start)
    

main()