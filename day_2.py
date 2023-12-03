from math import prod
from collections import Counter, defaultdict

# first, split by ":" to get separate the Game number and the balls
games = [line.split(":") for line in open("input/day_2.txt").readlines()]
games_and_scores = {}
for g in games:
    games_and_scores[g[0]] = g[1].strip().split(";")

counts = []
for game_num, scores in games_and_scores.items():
    for s in scores:
        total_count = 0
        for t in s.split(","):
            ball_count = t.strip().split(" ")
            count = ball_count[0]
            color = ball_count[1]
            counts.append({int(game_num.split(" ")[1]): {color: int(count)}})

merged_data = {}
for d in counts:
    for game, color_counts in d.items():
        if game not in merged_data:
            merged_data[game] = []

        merged_data[game].append(color_counts)


def part_one():
    filtered_games = set()
    filter_criteria = Counter(red=12, green=13, blue=14)

    for game, color_counts in merged_data.items():
        for c in color_counts:
            if any(count > filter_criteria[color] for color, count in c.items()):
                break
        else:
            filtered_games.add(game)

    print(sum(filtered_games))


def part_two():
    games = []
    for _, color_counts in merged_data.items():
        d = defaultdict(int)
        for color_count in color_counts:
            for k, v in color_count.items():
                d[k] = max(d[k], v)
        games.append(prod(d.values()))



    return sum(games)


print(part_two())
