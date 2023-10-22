s = str(input()).split()
l = len(set(s))
if l == 1:
    print("Все числа равны")
elif l == len(s):
    print("Все числа разные")
else:
    print("Есть равные и неравные числа")