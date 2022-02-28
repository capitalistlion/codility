# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
import time
import random

def solution(A):
    # write your code in Python 3.6
    return len(set(A))

A = []
for i in range(0,1*10**5):
    n = random.randint(-1*10**6,1*10**6)
    A.append(n)
print("done")
start_time = time.time()
print(solution(A))
end_time = time.time()
total_time = end_time - start_time
print("Time: ", total_time)

#CODILITY URL
#https://app.codility.com/demo/results/trainingPZSHXB-KX6/