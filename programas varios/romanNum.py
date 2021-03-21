# I = 1
# V = 5
# X = 10
# L = 50
# C = 100
# D = 500
# M = 1000
# 1 hasta 1000
# 292 = CC XC II
# 754 = DCC L IV
# I II III IV V VI VII VIII IX X

class py_solution:
    def int_to_Roman(self, num):
        val = [
            1000, 900, 600, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
            ]
        syb = [
            "M", "CM", "DC", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
            ]
        roman_num = ''
        i = 0
        while  num > 0:
            for _ in range(num // val[i]):
                roman_num += syb[i]
                num -= val[i]
            i += 1
        return roman_num


for i in range(1,1001):
    print(py_solution().int_to_Roman(i))




