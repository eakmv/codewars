def order(sentence):
    if not sentence:
        return sentence
    word_list = sentence.split(' ')
    result = []
    for w in range(len(word_list)):
        result.append(' ')
    for word in word_list:
        index = foo(word)
        result[index-1] = word
    return  ' '.join(result)


def foo(word):
    counter = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    for number in counter:
        if number in word:
            return int(number)
