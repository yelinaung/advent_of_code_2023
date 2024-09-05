def num(s: str) -> int:
    x = [c for c in s if c.isdigit()]
    return int(f"{x[0]}{x[-1]}")


def translate(s: str) -> str:
    nums = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    cov = ["o1e", "t2o", "t3e", "f4u", "f5r", "s6i", "s7e", "e8i", "n9e"]
    for num, c in zip(nums, cov):
        while num in s:
            s = s.replace(num, c)
    return s


lines = open("input.txt").readlines()
print(sum((num(translate(line)) for line in lines)))
