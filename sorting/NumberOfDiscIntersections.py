# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    N = len(A)
    if N == 0: return 0
    S = [0]*N
    E = [0]*N
    CS = [0]*N
    CE = [0]*N

    for J in range(N):
        S[J] = J - A[J] if J - A[J] > 0 else 0
        E[J] = J + A[J] if J + A[J] <= N-1 else N-1
        CS[S[J]] +=1
        CE[E[J]] +=1

    CCS = [0]*N
    CCE = [0]*N

    CCS[0] = CS[0]
    CCE[0] = CE[0]

    for J in range(1, N):
        CCS[J] = CCS[J-1] + CS[J]
        CCE[J] = CCE[J-1] + CE[J]

    sumOfIntersections = 0

    for J in range(N):
        if J==0:
            sumOfIntersections += ((CCS[J] - CS[J]) * CS[J]) + (CS[J] * (CS[J]-1)/2) # SECOND SUM INCLUDES MUTUAL INTERSECTIONS
        else:
            sumOfIntersections += ((CCS[J] - CCE[J-1] - CS[J]) * CS[J]) + (CS[J] * (CS[J]-1)/2) # SECOND SUM INCLUDES MUTUAL INTERSECTIONS

        if sumOfIntersections > 1*10**7: return -1

    return int(sumOfIntersections)

#CODILITY URL
#https://app.codility.com/demo/results/training3PBWK2-WSE/