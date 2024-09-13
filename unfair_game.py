# https://csacademy.com/contest/archive/task/unfair_game/
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

# MAIN CODE
# get inputs
size = get_number()
nums = []
sum = 0
for n in range(size):
    nums.append(get_number())
nums = sorted(nums)

# process it
i = size - 1
while i >= 0:
    sum += nums[i]
    i -= 1
    while nums[i] >= 0 or i % 2 == 1:
        sum += nums[i]
        i -= 1
    i -= 1

# output
print(sum)