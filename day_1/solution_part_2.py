import regex

with open("input.txt") as file:
    lines = file.readlines()


def replace_helper(input_lines):
    replaced_lines = []
    for line in input_lines:
        if "one" in line:
            line = line.replace("one", "1").strip()
        if "two" in line:
            line = line.replace("two", "2").strip()
        if "three" in line:
            line = line.replace("three", "3").strip()
        if "four" in line:
            line = line.replace("four", "4").strip()
        if "five" in line:
            line = line.replace("five", "5").strip()
        if "six" in line:
            line = line.replace("six", "6").strip()
        if "seven" in line:
            line = line.replace("seven", "7").strip()
        if "eight" in line:
            line = line.replace("eight", "8").strip()
        if "nine" in line:
            line = line.replace("nine", "9").strip()

        replaced_lines.append(line.strip())

    return replaced_lines


# kind of cheating here by using an external library
# to solve the problem of "12oneight"
def regex_helper(input_lines):
    matched_lines = []
    for line in input_lines:
        matched_lines.append(
            "".join(regex.findall(r"(one|two|three|four|five|six|seven|eight|nine|[0-9])", line, overlapped=True))
        )
    return matched_lines


replaced_lines = replace_helper(regex_helper(lines))
digits = []
for line in replaced_lines:
    digits.append([i for i in list(line.strip()) if i.isdigit()])

total = 0
for digit in digits:
    first = int(digit[0])
    if len(digit) == 1:
        total += int(f"{first}{first}")
    else:
        last = int(digit[-1])
        total += int(f"{first}{last}")

print(total)
