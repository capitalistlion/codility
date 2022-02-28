# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
import time
import random

def solution(A):
    # write your code in Python 3.6
    if len(A) < 3:
        return 0

    A.sort()
    for P in range(len(A)-2):
        if (A[P] + A[P+1]) > A[P+2]:
            print("pqr - "+str(P)+" "+str(P+1)+" "+str(P+2))
            print("A[pqr] - "+str(A[P])+" "+str(A[P+1])+" "+str(A[P+2]))
            return 1
        # where i>2. If A[P]+A[P+1] <= A[P+2],
        # then A[P]+A[P+1] <= A[P+i], where
        # i>=2. So there is no element in A[P+2:] that
        # could be combined with A[P] and A[P+1]
        # to be a triangular.
    return 0

A = []
for i in range(1*10**5):
    n = random.randint(-2.2*10**9,2.2*10**9)
    A.append(n)
start_time = time.time()
print(solution(A))
end_time = time.time()
total_time = end_time - start_time
print("Time: ", total_time)

#CODILITY URL
#https://app.codility.com/demo/results/trainingH6WB4J-JZE/