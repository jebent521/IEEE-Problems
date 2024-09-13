# https://csacademy.com/contest/archive/task/anagrams/
# a simple parser for python. use get_number() and get_word() to read
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

from collections import defaultdict

counts = defaultdict(int)
for i in range(get_number()):
    word = get_word()
    counts[''.join(sorted(word))] += 1
print(max(counts.values()))