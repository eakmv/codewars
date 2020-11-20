def alphabet_position(text):
    new_string = []
    for letter in text:
        index = ord(letter)-96
        if index >= 1 and index<=26:
            new_string.append(str(index))
        elif (index>=-31 and index<=-6):
            new_string.append(str(index+32))
        else:
            continue
    return ' '.join(new_string)