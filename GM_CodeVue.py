#given 2 numbers, find the least common multiple

def lcm(a: int, b: int):
    #c is lower num, d is higher
    c = (a if a < b else b)
    d = (a if a > b else b)

    i = 1
    lcm = 0
    while i <= d:
        curr = c*i
        if(curr%d == 0):
            lcm = curr
            break
        else:
            i+=1
    
    return lcm 

"""
import sys
#create a dictionary with num as key and occurrences as value.
#incrememt as u iterate through the list of numbers
#how to parse input thooo

def findOcc(numList):
    d = {}
    for i in nums:
        if (i in d.keys()):
            d[i] += 1
        else:
            d[i] = 1
    for k,v in d.items():
        print((('{} {} ').format(v, k)), end ="")

for line in sys.stdin:
    nums = line.split()
    if (len(nums) == 0):
        print("")
    else:
        findOcc(nums)




Programming challenge description:
Write a program that, given two clock times, prints out the absolute number of minutes between them.
Input:
Your program should read lines from standard input. Each line contains two wall clock times separated by a hyphen. Wall clock time is defined as hh:mm followed by AM' or 'PM', e.g. '09:05 AM'
Output:
Print to standard output the number of minutes between the two times from standard input. Print out each result on a new line.
Test 1
Test Input
10:00 AM - 11:00 AM
Expected Output
60
Test 2
Test Input
1:00 PM - 11:00 AM
Expected Output
1320
"""
