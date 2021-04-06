# 1504170715041707n mod 4503599627370517.
def eulercoin(n):
    return int((1504170715041707 * n) % 4503599627370517)


eulercoins = [1504170715041707]
for i in range(1, 1000):
    if eulercoin(i) < all(eulercoins):
        eulercoins.append(eulercoin(i))
# 1504170715041707 A
# 3008341430083414 A*2
# 8912517754604 C-A*2

print(eulercoin(1000))
print(sum(eulercoins))