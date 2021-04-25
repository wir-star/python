def get(n):
    if n < 1:
        return 0
    else:
        return get(n - 1) + n


print(get(5))
