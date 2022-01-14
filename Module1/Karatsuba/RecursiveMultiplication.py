'''Karatsuba multiplication algorithm

    Reference https://www.youtube.com/watch?v=yWI2K4jOjFQ for algorithm in python if unable to come up with solution
    
    Write out necessary terms first in psuedocode, then translate to a code structure.
    Point of this is to help with taking high level structure of algo and impelementing into code'''

x = 3141592653589793238462643383279502884197169399375105820974944592
y = 2718281828459045235360287471352662497757247093699959574966967627

print(x)


def recursive_multiply(x, y):
    if x < 10 or y < 10:
        return x*y
    
    # get number of digits from each x,y entry
    n = max(len(str(x)), len(str(y)))

    half = n//2
    #print(half)

    x1 = x//10**half
    x0 = x%10**half

    y1 = y//10**half
    y0 = y%10**half

    # recursive steps
    p = recursive_multiply(x1+x0, y1+y0)  
    
    x1y1 = recursive_multiply(x1, y1)
    x0y0 = recursive_multiply(x0, y0)

    return ((x1y1)*10**(2*half))+(p-x1y1-x0y0)*(10**(half))+x0y0
    

print(recursive_multiply(x,y))




