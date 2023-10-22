alphabet = 'abcdefghijklmnopqrstuvwxyz'
inp = str(input())
symbol = inp[:1]
shift = int(inp[2:])
number = 0
for i in range(26):
    if symbol == alphabet[i]:
        number = i
        print(alphabet[number+shift])