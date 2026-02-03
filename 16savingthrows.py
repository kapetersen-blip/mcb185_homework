import random

def saving_throw(dc, mode="normal"):
    if mode == "normal":
        roll = random.randint(1, 20)
    elif mode == "advantage":
        roll = max(random.randint(1, 20), random.randint(1, 20))
    elif mode == "disadvantage":
        roll = min(random.randint(1, 20), random.randint(1, 20))

    success = roll >= dc
    return roll, success


dcs = [5, 10, 15]
modes = ["normal", "advantage", "disadvantage"]

for dc in dcs:
    print(f"\nDC {dc}")
    for mode in modes:
        roll, success = saving_throw(dc, mode)
        result = "SUCCESS" if success else "FAIL"
        print(f"{mode.capitalize():12} Roll: {roll} → {result}")

