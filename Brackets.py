# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    # write your code in Python 3.6
    if len(S) == 0: return 1
    openBrackets = ["{", "[", "("]
    closedBrackets = ["}", "]", ")"]
    bracketIndex = []
    for currentBracket in S:
        if currentBracket in openBrackets:
            bracketIndex.append(openBrackets.index(currentBracket)+1)
        else:
            if not bracketIndex:
                return 0
            # if previous number is also negative then check if a positive one exists in the index
            if bracketIndex[-1] < 0:
                if closedBrackets.index(currentBracket)+1 not in bracketIndex: return 0
                bracketIndex.append(-1*(closedBrackets.index(currentBracket)+1))
            else:
                if bracketIndex[-1] - (closedBrackets.index(currentBracket)+1) != 0: return 0
                bracketIndex.append(-1*(closedBrackets.index(currentBracket)+1))

    if sum(bracketIndex) != 0: return 0
    return 1

#CODILITY URL
#https://app.codility.com/demo/results/training5DDGWC-94Y/