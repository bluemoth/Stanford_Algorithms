'''Algorithm implementation for inversion counting.
   The algorithm to be used will be from Algorithm By Design textbook
   Larger file contained within IntegerArray'''

line_number = 0
homeWorkList = []

with open('IntegerArray.txt', encoding="utf-8") as a_file:
    for line in a_file:
        numbers_str = line.split()
        #print(numbers_str)
        homeWorkList += [int(x) for x in numbers_str]
        #print(homeWorkList)
        #work with numbers_float here


def MergeAndCount(a,b):
    count = 0 # variable to count inversions
    sortedList = []

    # pointers to point to first elements in lists
    i = 0
    j = 0

    # compare & merge
    while len(a) > i and len(b) > j:
        if a[i] < b[j]: # indicates left array is larger
            sortedList.append(a[i])
            i += 1
        else:
            sortedList.append(b[j])
            j += 1
            count += (len(a)-i)
            
    sortedList += a[i:]
    sortedList += b[j:]
    return count, sortedList
    

def SortAndCount(list):
    # get length of list
    n = len(list)
    # half length
    half = n // 2 

    # single element, no inversion, return list
    if len(list) <= 1:  
        return 0, list
    else:    
        # array len > 1, divide in half
        a = list[:half]
        b = list[half:]

        # perform recursions; format is count, list return
        cA, a = SortAndCount(a)
        cB, b = SortAndCount(b)
        c, sL = MergeAndCount(a,b)
        c = cA + cB + c
    
        return c, sL


x, y = SortAndCount(homeWorkList)
print(x)


