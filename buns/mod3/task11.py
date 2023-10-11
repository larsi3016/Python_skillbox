s1 = str(input())
s2 = str(input())
s3 = str(input())
for i in range(3):
    if s1[i] == s2[i] == s3[i]:
        print(s1[i])
    elif len(set(s1)) == 1:
        print(s1[0])
    elif len(set(s2)) == 1:
        print(s2[0])
    elif len(set(s3)) == 1:
        print(s3[0])
    elif s1[0] == s2[1] == s3[2]:
        print(s1[0])
    elif s1[2] == s2[1] == s3[0]:
        print(s1[2])