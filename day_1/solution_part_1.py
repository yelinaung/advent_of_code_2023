with open("input.txt") as file:
    lines = file.readlines()

digits = []
for line in lines:
    digits.append([i for i in list(line.strip()) if i.isdigit()])

total = 0
for digit in digits:
    first = int(digit[0])
    if len(digit) == 1:
        total += int(f"{first}{first}")
    else:
        total += int(f"{first}{digit[-1]}")

print(total)
