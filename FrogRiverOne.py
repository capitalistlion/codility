# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(X, A):
    i = 0
    uniqueLeaves = {}
    while i < len(A):
        uniqueLeaves[A[i]] = i
        if len(uniqueLeaves) == X:
            return i
        i += 1
    return -1
