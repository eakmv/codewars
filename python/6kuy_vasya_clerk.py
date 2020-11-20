"""
https://www.codewars.com/kata/vasya-clerk/train/python
"""

def tickets(people):
    cashbox = {25:0, 50:0, 100:0}
    for p in people:
        if p == 25:
            cashbox[25] += 1
        if p == 50:
            if cashbox[25] == 0:
                return "NO"
            cashbox[50] += 1
            cashbox[25] -= 1
        if p == 100:
            if cashbox[25] == 0:
                return "NO"
            cashbox[100]+=1
            if cashbox[50] >= 1 and cashbox[25] >= 1:
                cashbox[50] -= 1
                cashbox[25] -= 1
            elif cashbox [25] >= 3:
                cashbox[25] -= 3
            else:
                return "NO"

    return "YES"
