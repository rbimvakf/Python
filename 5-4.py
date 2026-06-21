numbers = [1, -2, 3, -5, 8, -3]

def check(a):
    return a > 0
print(list(filter(check, numbers)))
# [1, 3, 8]
print(list(filter(lambda a: a > 0, numbers)))
# [1, 3, 8]
