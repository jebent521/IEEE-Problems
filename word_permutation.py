# https://csacademy.com/contest/archive/task/word_permutation/
def parser():
    while 1:
        data = list(input().split(' '))
        for number in data:
            if len(number) > 0:
                yield(number)   

input_parser = parser()

def get_word():
    global input_parser
    return next(input_parser)

def get_number():
    data = get_word()
    try:
        return int(data)
    except ValueError:
        return float(data)

n = get_number()
words = []
for i in range(n):
    words.append(get_word())
in_order = sorted(words)
for word in in_order:
    print(words.index(word) + 1, end=" ")

