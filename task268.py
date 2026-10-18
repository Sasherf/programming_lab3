n = int(input())
count = 1

for i in range(n):
    for j in range(count):
        print(j + 1, end="")
    print()
    count += 1