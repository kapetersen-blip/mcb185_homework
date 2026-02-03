import random

def death_save():
    successes = 0
    failures = 0

    while True:
        roll = random.randint(1, 20)

        if roll == 1:
            failures += 2
        elif roll == 20:
            return "revive"
        elif roll >= 10:
            successes += 1
        else:
            failures += 1

        if failures >= 3:
            return "die"
        if successes >= 3:
            return "stabilize"


# run the simulation
trials = 100000
results = {"die": 0, "stabilize": 0, "revive": 0}

for _ in range(trials):
    outcome = death_save()
    results[outcome] += 1

# print probabilities
for outcome in results:
    probability = results[outcome] / trials
    print(f"{outcome.capitalize()}: {probability:.3f}")

