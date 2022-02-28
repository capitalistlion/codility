# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
from functools import reduce
import time
import random

def solution(A):
    # write your code in Python 3.6
    A.sort()
    return max(A[0]*A[1]*A[-1], A[-1]*A[-2]*A[-3])

A = []
for i in range(3,1*10**5):
    n = random.randint(-1*10**5,1*10**5)
    A.append(n)
start_time = time.time()
print(solution(A))
end_time = time.time()
total_time = end_time - start_time
print("Time: ", total_time)

#CODILITY URL
#https://app.codility.com/demo/results/trainingSVQ9ZP-QBJ/