import sys

alphabet = sys.argv[1]
match = int(sys.argv[2])
mismatch = int(sys.argv[3])

# Print header row
print(" ", end="")
for base in alphabet:
    print(f" {base}", end="")
print()

# Print matrix rows
for row in alphabet:
    print(row, end="")
    for col in alphabet:
        if row == col:
            print(f" {match}", end="")
        else:
            print(f" {mismatch}", end="")
    print()
