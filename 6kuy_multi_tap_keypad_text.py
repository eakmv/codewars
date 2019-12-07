def num_press(let):
    alphabet =\
        {1: ['a', 'd', 'g', 'j', 'm', 'p', 't', 'w', '*', ' ', '#', '1'],
         2: ['b', 'e', 'h', 'k', 'n', 'q', 'u', 'x', '0'],
         3: ['c', 'f', 'i', 'l', 'o', 'r', 'v', 'y'],
         4: ['s', 'z', '2', '3', '4', '5', '6', '8'],
         5: ['7', '9'],
         }
    for key, v in alphabet.items():
        if let in v:
            return key


def presses(phrase):
    answer = 0
    for let in phrase:
        answer += num_press(let.lower())
    return answer