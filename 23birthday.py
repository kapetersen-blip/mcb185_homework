import random
import sys

# Command-line arguments
trials = int(sys.argv[1])
days = int(sys.argv[2])
people = int(sys.argv[3])

matches = 0

for _ in range(trials):
    birthdays = []
    duplicate = False

    for _ in range(people):
        bday = random.randrange(days)

        if bday in birthdays:
            duplicate = True
            break
        birthdays.append(bday)

    if duplicate:
        matches += 1

# Calculate probability
probability = matches / trials

print(probability)
