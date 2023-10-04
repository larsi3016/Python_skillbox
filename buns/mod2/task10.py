s = str(input())
output = ''
for i in range(len(s)):
    if s[i] == ' ':
        output += s[i-1]
output += s[-1]
print(output)