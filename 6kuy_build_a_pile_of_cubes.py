"""
https://www.codewars.com/kata/5592e3bd57b64d00f3000047
"""

def find_nb(m):
    summa = 0
    count = 1
    while summa < m:
        summa = summa + count**3
        count+=1
    if summa!=m:
        return -1
    else:
        return count-1
