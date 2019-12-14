"""
https://www.codewars.com/kata/55b4d87a3766d9873a0000d4
"""

def isInt(n):
    return int(n) == float(n)

def howmuch(m, n):
    if m > n:
        m, n = n,m
    answer = []
    for s in list(range(m, n+1)):
        b = (s-2)/7
        c = (s-1)/9
        if isInt(b) and isInt(c):
            answer.append(["M: " + str(s), "B: " + str(int(b)), "C: " + str(int(c))])

    return answer
