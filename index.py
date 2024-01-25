def func(x):
    count = 0
    while x:
        count += 1
        x //=10
    return count
print(func(12))