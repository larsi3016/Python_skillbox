s = str(input())
symbol = s[-1]
counter = 0
flag = 1
i = 0
while flag:
    if s[i] == symbol:
        counter += 1
    else:
        flag = 0
    i += 1
print(counter)