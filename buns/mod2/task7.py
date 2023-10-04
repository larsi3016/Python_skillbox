s = str(input())
counter0 = 0
counter1 = 0
for i in range(len(s)):
    if s[i] == '0':
        counter0 += 1
    else:
        counter1 += 1
if counter1 == counter0:
    print('yes')
else:
    print('no')