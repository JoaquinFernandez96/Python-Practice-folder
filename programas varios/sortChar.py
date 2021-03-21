'''
lista_og=["aaa","aaaa","aa"]
sol= sorted(lista_og, key=len)
print(sol)
'''


lista_og = [
    "z",
    "hola",
    "xd",
    "cha",
    "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",
    "xxxxx",
    "x",
    "dd",
    "xxxxxxxxxxx",
]


def insertar(lista, m, elem):
    lista.insert(m, elem)
    return lista


def xdsort(k):
    if len(k) == 2:
        if k[0] > k[1]:
            return [k[1], k[0]]
        else:
            return [k[0], k[1]]
    else:
        lens = []
        for i in k:
            lens.append(len(i))

        sortedlens = sorted(lens)
        index = sortedlens.index(len(k[0]))

        return insertar(xdsort(k[1:]), index, k[0])


print(xdsort(lista_og))