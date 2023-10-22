s = str(input())
digCounter = 0
for i in range(len(s)):
    if s[i] == '-' or s[i] == '(' or s[i] == ')' or s[i] == ' ':
        digCounter += 1
i = 0
while i < len(s):
    if s[i] == '-' or s[i] == '(' or s[i] == ')' or s[i] == ' ':
        s = s[:i:] + s[i+1::]
        i-=1
    i+=1
print(s)
