line_number = 0
homeWorkList = []

with open('QuickSort.txt', encoding="utf-8") as a_file:
    for line in a_file:
        numbers_str = line.split()
        #print(numbers_str)
        homeWorkList += [int(x) for x in numbers_str]
        #print(homeWorkList)
        #work with numbers_float here
        

'''First objective is count number of comparisons always using the first element of the QuickSort array. Do not count comparisons
   one-by-one. Instead, when recursive call is made on sub-array m, add m-1 to bypass counting one by one.'''

testListOne = [4,5,2,3,1] # of comparison = 7,8,6, 
testListTwo = [3,2,10,6,7,1,9,5,4,8] # of comparisons = 21, 22, 20
tl2 = len(testListTwo)
tl1 = len(testListOne) 
hml = len(homeWorkList)

def Quicksort_First(A, l, r):
    global countFirst
    if l < r:
        countFirst += (r-l-1)
        print(r-l-1)
        p = Partition_First(A, l, r)
        Quicksort_First(A, l, p)
        Quicksort_First(A, p+1, r)
        return countFirst

def Quicksort_Last(A, l, r):
    global countLast
    if l < r:
        countLast += (r-l-1)
        #print(r-l-1)
        p = Partition_Last(A, l, r)
        Quicksort_Last(A, l, p)
        Quicksort_Last(A, p+1, r)
        return countLast

def Quicksort_Median(A, l, r):
    global countMedian
    if l < r:
        countMedian += (r-l-1)
        #print(r-l-1)
        p = Partition_Median(A, l, r)
        Quicksort_Median(A, l, p)
        Quicksort_Median(A, p+1, r)
        return countMedian

def Partition_First(A, l, r):
    #print(A[l:r])
    # assign pivot
    pivot = A[l]
    # i and j, selecting element immediately after pivot
    i = j = l + 1
    for j in range(j, r): # j walk through elements
        if A[j] < pivot: # compare j element vs pivot
            A[i], A[j] = A[j], A[i] # if less than pivot, swap values of j and i now that both are compared
            i += 1
    A[l], A[i-1] = A[i-1], A[l] # after j walks off end of array, then swap the pivot with i-1
    return i-1 # this is the new location of the pivot element after the final swap of pivot and step above

def Partition_Last(A, l, r):
    #print(A[l:r)
    # assign pivot
    pivot = A[r-1]

    #from homework, should swap left end and right end of element
    A[l], A[r-1] = A[r-1], A[l]

    # i and j, selecting element immediately after pivot
    i = j = l+1
    for j in range(j, r): # j walk through elements
        if A[j] < pivot: # compare j element vs pivot
            A[i], A[j] = A[j], A[i] # if less than pivot, swap values of j and i now that both are compared
            i += 1
    A[l], A[i-1] = A[i-1], A[l] # after j walks off end of array, then swap the pivot with i-1
    return  i-1 # this is the new location of the pivot element after the final swap of pivot and step above

def Partition_Median(A, l, r):
    # setup median function
    left = A[l]
    right = A[r-1]
    length = r - l
    
    if length % 2 == 0:
        middle = A[l + int(length/2)-1]
    else:
        middle = A[l + int(length/2)]

    # assign pivot
    pivot = findMedian(left, middle, right)
    pivotindex = A.index(pivot)
    #from assignment, should swap pivot with left end
    A[l], A[pivotindex] = pivot, A[l]

    # i and j, selecting element immediately after pivot
    i = j = l+1
    for j in range(j, r): # j walk through elements
        if A[j] < pivot: # compare j element vs pivot
            A[i], A[j] = A[j], A[i] # if less than pivot, swap values of j and i now that both are compared
            i += 1
    A[l], A[i-1] = A[i-1], A[l] # after j walks off end of array, then swap the pivot with i-1
    return  i-1 # this is the new location of the pivot element after the final swap of pivot and step above

def findMedian(a, b, c):
    if ((a > b) ^ (a > c)):
        return a
    elif ((b < a) ^ (b < c)):
        return b
    else:
        return c
  



countFirst = 0
countLast = 0
countMedian = 0


'''Quicksort with last element'''
# print(testListOne, tl1)
# r = Quicksort_First(testListOne, 0, tl1)
# print(testListOne)
# print(r) # result = 7

# print(testListTwo)
# r = Quicksort_First(testListTwo, 0, tl2)
# print(testListTwo)
# print (r) # result = 21

# r = Quicksort_First(homeWorkList, 0, hml)
# print(homeWorkList)
# print(r) # result = 162085

'''Quicksort with last element'''
# print(testListOne, tl1)
# r = Quicksort_Last(testListOne, 0, tl1)
# print(testListOne)
# print(r) # result = 8

# print(testListTwo)
# r = Quicksort_Last(testListTwo, 0, tl2)
# print(testListTwo)
# print (r) # result = 22

# r = Quicksort_Last(homeWorkList, 0, hml)
# print(homeWorkList)
# print(r) # result = 164123

'''Quicksort with median element'''
# print(testListOne, tl1)
# r = Quicksort_Median(testListOne, 0, tl1)
# print(testListOne)
# print(r) # result = 6

# print(testListTwo)
# r = Quicksort_Median(testListTwo, 0, tl2)
# print(testListTwo)
# print (r) # result = 20

r = Quicksort_Median(homeWorkList, 0, hml)
print(homeWorkList)
print(r) # result = ????