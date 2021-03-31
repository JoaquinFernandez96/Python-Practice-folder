import sympy
from itertools import permutations


def join_tuple_string(strings_tuple) -> str:
    return " ".join(strings_tuple)


numeros = ["1", "2", "3", "4", "5", "6", "7"]

primos = []
pandigits1 = list(permutations(numeros))
pandigits2 = []
for i in pandigits1:
    pandigits2.append(int(join_tuple_string(i).replace(" ", "")))


for j in pandigits2:
    if sympy.ntheory.primetest.isprime(j):
        print(j)

# sympy.ntheory.primetest.isprime