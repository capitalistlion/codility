# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
import random

def solution(A):
    # write your code in Python 3.6
    east = 0
    passes = 0
    for i in A:
        if i == 0:
            east += 1
        else:
            passes += east
        if passes > 1000000000: return -1
    return passes

A = []
for i in range(0,100000):
    n = random.randint(0,1)
    A.append(n)

print(solution(A))