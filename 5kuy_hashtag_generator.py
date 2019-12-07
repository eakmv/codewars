def generate_hashtag(s):
    if len(s) > 140:
        return False
    answer = "#"
    up_flag = True
    for char in s:
        if char == ' ':
            up_flag = True
            continue
        else:
            if up_flag:
                answer = answer + char.upper()
                up_flag = False
            else:
                answer = answer + char.lower()

    if answer != "#":
        return answer
    else:
        return False