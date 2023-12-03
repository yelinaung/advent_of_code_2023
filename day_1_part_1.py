with open("input/day_1.txt") as file:
    lines = file.readlines()

digits = []
for line in lines:
    digits.append([i for i in list(line.strip()) if i.isdigit()])

total = 0
for digit in digits:
    total += int(f"{digit[0]}{digit[-1]}")

print(total)
