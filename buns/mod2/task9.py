vowels = 'аеёиоуыэюя'
consonants = 'бвгджзйклмнпрстфхчцшщ'
s = str(input())
Vcounter = 0
Ccounter = 0
for i in range(len(s)):
     if s[i] in vowels:
         Vcounter += 1
     if s[i] in consonants:
         Ccounter += 1
print(Vcounter,Ccounter)