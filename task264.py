n = int(input("Enter the number of participants: "))
max_answers = -1
zero_count = 0

for i in range(n):
    right_answers = int(input())
    if right_answers > max_answers:
        max_answers = right_answers
    if right_answers == 0:
        zero_count += 1

print(f"The winner has {max_answers} right answers.")
if zero_count > 0:
    print("Yes")
else:
    print("No")