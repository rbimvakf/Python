import random

numbers = [i for i in range(1, 46)]

def lottery(data):
    number = random.choice(data)
    data.remove(number)
    return number

result = [lottery(numbers) for i in range(6)]
result.sort()

print("당첨번호: ", end = "")

for i in range(6):
    print("%d " % result[i], end = "")
