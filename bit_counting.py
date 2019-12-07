def countBits(n):
    value = str(bin(n)[2:])
    count = 0
    for a in value:
        if a=='1':
            count+=1
    return count