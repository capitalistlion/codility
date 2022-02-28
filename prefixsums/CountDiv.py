# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

import random
import time

def solution(A, B, K):
    if B - A > 2*10**6:
        listRange = list(range(A,2*10**6+1))
        listRangeMod = list(filter(lambda a: a % K == 0, listRange))
        count = len(listRangeMod)
        if B > 2*10**7+1:
            listRange = list(range(2*10**6+2,2*10**7+1))
            listRangeMod = list(filter(lambda a: a % K == 0, listRange))
            count += len(listRangeMod)
        elif B > 2*10**8+1:
            listRange = list(range(2*10**7+2,2*10**8+1))
            listRangeMod = list(filter(lambda a: a % K == 0, listRange))
            count += len(listRangeMod)
        else:
            listRange = list(range(2*10**8+2,B))
            listRangeMod = list(filter(lambda a: a % K == 0, listRange))
            count += len(listRangeMod)

    else:
        listRange = list(range(A,B+1))
        listRangeMod = list(filter(lambda a: a % K == 0, listRange))
        count = len(listRangeMod)
    return count

A = random.randint(0,2*10**6)
B = random.randint(A,2*10**6)
K = random.randint(A,2*10**6)
print("A - "+str(A))
print("B - "+str(B))
print("K - "+str(K))
start_time = time.time()
print(solution(6, 11, 2))
end_time = time.time()
total_time = end_time - start_time
print("Time: ", total_time)