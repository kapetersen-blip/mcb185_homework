import sys
import math

def main():
    # Convert command-line arguments to floats
    try:
        numbers = [float(x) for x in sys.argv[1:]]
    except ValueError:
        print("Please provide only numeric values.")
        return

    if len(numbers) == 0:
        print("Usage: python stats.py <numbers>")
        return

    n = len(numbers)
    minimum = min(numbers)
    maximum = max(numbers)
    mean = sum(numbers) / n

    # Sample standard deviation
    if n > 1:
        variance = sum((x - mean) ** 2 for x in numbers) / (n - 1)
        std_dev = math.sqrt(variance)
    else:
        std_dev = 0.0

    # Median
    numbers.sort()
    mid = n // 2
    if n % 2 == 0:
        median = (numbers[mid - 1] + numbers[mid]) / 2
    else:
        median = numbers[mid]

    print(f"Count: {n}")
    print(f"Min: {minimum}")
    print(f"Max: {maximum}")
    print(f"Mean: {mean}")
    print(f"Standard Deviation: {std_dev}")
    print(f"Median: {median}")

if __name__ == "__main__":
    main()
