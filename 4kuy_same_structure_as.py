"""
https://www.codewars.com/kata/nesting-structure-comparison/train/python
"""

def find_structure(s):
    if not isinstance(s, list):
        return type(s)
    else:
        res = []
        for b in s:
            if isinstance(b, list):
                res.append(find_structure(b))
            else:
                res.append(type(b))
        return res

def same_structure_as(original, other):
    if original == other:
        return True
    orig_structure = find_structure(original)
    other_structure = find_structure(other)
    if orig_structure == other_structure:
        return True
    else:
        return False