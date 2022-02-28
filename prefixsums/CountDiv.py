# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

import random
import time

def solution(A, B, K):
    edge = 1 if A % K == 0 else 0
    return B // K - A // K + edge

A = random.randint(0,2*10**6)
B = random.randint(A,2*10**6)
K = random.randint(A,2*10**6)
print("A - "+str(A))
print("B - "+str(B))
print("K - "+str(K))
start_time = time.time()
print(solution(100, 10**9, 2))
end_time = time.time()
total_time = end_time - start_time
print("Time: ", total_time)