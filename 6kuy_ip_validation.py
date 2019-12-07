def is_valid_IP(strng):
    for n in strng:
        if n.isspace():
            return False
    new_ip = strng.split('.')
    if len(new_ip)!=4:
        return False
    for oct in new_ip:
        try:
            if 0<=int(oct)<=255 and oct[0] != '0':
                continue
            else:
                return False
        except ValueError:
            return False

    return True