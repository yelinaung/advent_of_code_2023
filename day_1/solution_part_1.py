def num(s: str) -> int:
    x = [c for c in s if c.isdigit()]
    return int(f"{x[0]}{x[-1]}")


lines = open("input.txt").readlines()
total = sum([num(line) for line in lines])

# total = 0
# for digit in digits:
#     total += int(f"{digit[0]}{digit[-1]}")

print(total)
