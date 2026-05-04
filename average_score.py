def average(scores: [list]):
    total = 0

    for num in scores:
        total += num

    return (total / len(scores), 1)

scores = [84, 73, 92, 95, 88]

avg_score = average(scores)

print(round(avg_score, 1))