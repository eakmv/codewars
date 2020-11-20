"""
https://www.codewars.com/kata/5842df8ccbd22792a4000245
"""

def expanded_form(num):
    fin_list=[]
    count = len(str(num))
    fin_str=''
    for a in str(num):
        if a!='0':
            fin_list.append(int(10**(count-1)) * int(a))
        count-=1
    for a in fin_list:
        fin_str+=str(a)+' + '
    return(fin_str.strip(' +'))
