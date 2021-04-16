# 1504170715041707n mod 4503599627370517.
# solucion=1517926517777556
# 1504170715041707 
# 3008341430083414 
# 8912517754604 

def eulercoin(n):
    return int((1504170715041707 * n) % 4503599627370517)


def euclid(a,b):
    if a<b:
        a,b=b,a
    while b != 1:
        r=a%b
        mods.append(r)
        a=b
        b=r
    return mods

def modinv(n,m):
    return pow(n, -1, m)

a=1504170715041707
b=4503599627370517


def e700(n):
    E=a-(b%a)
    return E


print(res)


