def rot13(message):
    answer = ""
    for char in message:
        code = ord(char)
        if 97 <= code < 110 or 65 <= code < 78:
            answer = answer + chr(code + 13)
        elif 110 <= code <= 122 or 78 <= code < 90:
            answer = answer + chr(code - 13)
        else:
            answer = answer + char

    return answer