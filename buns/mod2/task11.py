s = str(input())
flag = 0
for i in range(len(s)):
    dig = s[0]
    s = s[1::]
    if dig in s:
        print(True)
        flag = 1
        break
if flag == 0:
    print(False)
