i = 0
while True:
    i += 1
    if i > 3:
        break
    print(" " * (3 - i), end="")
    print("*" * (2 * i - 1))
i = i - 1
while True:
    i -= 1
    if i < 0:
        break
    print(" " * (3 - i), end="")
    print("*" * (2 * i - 1))
'''
  *
 ***
*****
 ***
  *
'''
