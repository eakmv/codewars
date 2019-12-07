def toJadenCase(string):
    string=string.split(' ')
    jaden_string = []
    for word in string:
        new=word[0].upper()+word[1:]
        jaden_string.append(new)
    answ =' '.join(jaden_string)
    return answ