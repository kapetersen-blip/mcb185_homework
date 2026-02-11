import random
import sys

trials = int(sys.argv[1])
days = int(sys.argv[2])
people = int(sys.argv[3])

matches = 0

for _ in range(trials):
    calendar = [0] * days
    duplicate = False

    for _ in range(people):
        birthday = random.randrange(days)
        calendar[birthday] += 1

        if calendar[birthday] > 1:
            duplicate = True
            break

    if duplicate:
        matches += 1

probability = matches / trials
print(probability)
