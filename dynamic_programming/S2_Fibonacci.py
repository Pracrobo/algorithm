cache = [-1] * 91
cache[0] = 0
cache[1] = 1
cnt = 0
def f(n):
    global cnt
    cnt+= 1
    if n == 0:
        return 0
    elif n == 1:
        return 1

    return f(n-2) + f(n-1)


print(f(int(input())))
print(f'cnt: {cnt}')
