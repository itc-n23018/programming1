x = True
y = False
z = None

result = x and z is None
print(result)

aresult = not x or not y
print(aresult)

bresult = x and not y and z is None
print(bresult)
