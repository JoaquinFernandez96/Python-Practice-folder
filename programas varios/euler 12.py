from functools import reduce

limit = 10 ** 8


def factors(n):
    x = sorted(
        list(
            reduce(
                list.__add__,
                ([i, n // i] for i in range(1, int(n ** 0.5) + 1) if n % i == 0),
            )
        )
    )
    return x.pop(1)


# for i in range(1, limit + 1):
#     factors(i)

print(factors(7))
# LIMIT: 10**8
# 1 a 30: 10 [4, 6, 9, 10, 14, 15, 21, 22, 25, 26]
