# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
import random

def solution(N, A):
    # write your code in Python 3.6
    counters = [0]*N
    lastMaxCount = maxValue = 0
    for element in A:
        if element < N+1:
            if counters[element-1] < lastMaxCount:
                counters[element-1] = lastMaxCount
            counters[element-1] += 1
            if counters[element-1] > maxValue:
                maxValue = counters[element-1]
        else:
            lastMaxCount = maxValue

    for i in range(len(counters)):
        if counters[i] < lastMaxCount:
            counters[i] = lastMaxCount
    return counters

A = []
for i in range(0,100000):
    n = random.randint(1,100000)
    A.append(n)

print(solution(100000, A))