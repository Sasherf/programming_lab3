n = int(input())
count = 0
for i in range(1, n + 1):
    for j in range(i):
        if count < n:
            print(i, end=' ')
            count += 1