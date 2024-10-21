# I used ChatGPT to speed up the code in word_permutation.py
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

# Reading the first input number
n = get_number()

# Collect words
words = [next(input_parser) for _ in range(n)]

# Get sorted order and store original indices
sorted_words = sorted((word, i + 1) for i, word in enumerate(words))

# Output the original indices in sorted order
print(" ".join(str(index) for word, index in sorted_words))