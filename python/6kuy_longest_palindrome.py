'''
https://www.codewars.com/kata/longest-palindrome-1/python
'''


def longest_palindrome(s):
    if len(s) == 1:
        return 1
    if len(s) == 0:
        return 0

    init_dict = {ch : 0 for ch in s.lower() if ch.isdigit() or ch.isalpha()}
    for ch in s.lower():
        if str(ch) in init_dict.keys():
            init_dict[str(ch)] += 1

    result = 0
    odd_flag = True
    for a in init_dict.values():
        if a % 2 == 0:
            result += a
        elif a % 2 == 1:
            if odd_flag:
                result += a
                odd_flag = False
            elif a != 1:
                result += a - 1
    return result