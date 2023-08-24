import random

random.seed(1)
msgs = [
    "hi",
    "hello",
    "good morning",
    "see you later",
    "how are you",
    " have a good day",
]
with open("some.txt", "w") as f:
    for i in range(1000000):
        f.write("{}, {}\n".format(i, random.choice(msgs)))
%%time
f = open('some.txt')
c = 0
 for l in f:
      print(l, end='')
       if c == 2:
            break
        c += 1
        f.close()
