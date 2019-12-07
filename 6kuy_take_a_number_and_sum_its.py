def sum_dig_pow(a, b): # range(a, b + 1) will be studied by the function
    number_list = []
    start = a
    while start <= b:
        number_list.append(start)
        start+=1
    return list(filter(check_number, number_list))


def check_number(x):
    summa = 0
    count = 1
    for a in str(x):
        summa+=int(a)**count
        count+=1
    if summa == x :
        return True
    else:
        return False