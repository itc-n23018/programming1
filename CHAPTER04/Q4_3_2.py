def func_square(*args):
    results = []
    for n in args:
        results.append(n * n)
    return results


numbers = list(range(100))
print(func_square(*numbers))
