# is_heteromecic(0) ➞ True
# # 0 * (0 + 1) = 0 * 1 = 0
# is_heteromecic(2) ➞ True
# # 1 * (1 + 1) = 1 * 2 = 2
# is_heteromecic(7) ➞ False
# is_heteromecic(110) ➞ True
# # 10 * (10 + 1) = 10 * 11 = 110
# is_heteromecic(136) ➞ False
# is_heteromecic(156) ➞ True
n = 2


def is_heteromecic(n):
    pronic = False
    if n == 0:
        pronic = True
    else:
        for i in range(1, int(n ** 0.5) + 1):
            if i * (i + 1) == n:
                pronic = True
    return pronic


print(is_heteromecic(n))