# https://csacademy.com/contest/archive/task/moving_segments/
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

endpoints = []
segments = []
n = get_number()
for _ in range(n):
    x1 = get_number()
    x2 = get_number()
    endpoints.append(x1)
    endpoints.append(x2)
    segments.append((x1, x2))
endpoints.sort()
line = endpoints[n] # grab median
cost = 0
for segment in segments:
    # calculate distance from segment to line
    if segment[1] < line:
        cost += line - segment[1]
    elif segment[0] > line:
        cost += segment[0] - line
    
print(cost)
    