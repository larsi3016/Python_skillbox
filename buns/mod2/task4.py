a = float(input("Введите натуральное число"))
abin = ''
aoct = ''
ahex = ''
hex_digits = "0123456789ABCDEF"
if a != int(a):
    print("Неверный ввод")
else:
    a1 = int(a)
    a2 = int(a)
    a3 = int(a)
    while a1 > 0:
        abin = str(a1 % 2) + abin
        a1 = a1 // 2
    while a2 > 0:
        aoct = str(a2 % 8) + aoct
        a2 //= 8
    while a3 > 0:
        ahex = hex_digits[a3 % 16] + ahex
        a3 //= 16
print(abin, aoct, ahex)
