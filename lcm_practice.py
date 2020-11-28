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
