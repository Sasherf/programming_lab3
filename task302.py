a = int(input())
b = int(input())

start = (a - 1) + (a % 2)

for i in range(start, b - 1, -2):
    print(i, end=" ")