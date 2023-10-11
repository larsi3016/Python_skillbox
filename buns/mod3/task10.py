k = int(input())
for i in range(1, k+1):
    for j in range(1, k+1):
        if j == k:
            print(j)
        else:
            print(j, end=', ')
print()
for i in range(1, k+1):
    for j in range(1, k+1):
        if j == k:
            print(i)
        else:
            print(i, end=', ')