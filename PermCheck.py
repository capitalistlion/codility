# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    B = set(A)
    if len(A) != len(B): return 0

    #BELOW CODE IS IF THE ARRAY A HAS THE SAME NUMBER OF ELEMENTS IF IT WHERE UNIQUE
    maxNum = max(A)
    if maxNum+1 <= 10**6:
        Z = set(list(range(1,maxNum+1)))
        if B != Z: return 0
    else:
        Z = set(list(range(1,10**6)))
        if B != Z: return 0
        for i in range(1,maxNum+1):
            if i  not in A:
                return 0
                
    return 1
