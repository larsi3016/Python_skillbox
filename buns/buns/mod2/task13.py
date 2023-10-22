s = str(input())
s1 = s[::2]
s2 = s[1::2]
sum1 = 0
sum2 = 0
for i in range(len(s1)):
    sum1 += int(s1[i])
for i in range(len(s2)):
    sum2 += int(s2[i])
if (sum1 + 3*sum2) % 10 == 0:
    print("yes")
else:
    print("no")