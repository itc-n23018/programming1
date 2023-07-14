import random

numbers = list(range(0, 10))
sample4 = random.sample(numbers, k=4)
num4 = "".join(str(num) for num in sample4)
while True:
    val = input()
    if val == num4:
        print("OK")
        break
    else:
        print(val, ":NG")
