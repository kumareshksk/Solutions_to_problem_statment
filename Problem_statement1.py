import numpy as np
from fractions import Fraction

# Part 1: Total combinations
total_combinations = 6 * 6
print(f"Total combinations: {total_combinations}")

# Part 2: Distribution of All Possible Combinations
# Generate a 6x6 matrix for the sums of the dice rolls
sums_matrix = np.zeros((6, 6), dtype=int)

# Populate the matrix with sums
for i in range(6):
    for j in range(6):
        sums_matrix[i, j] = (i + 1) + (j + 1)

print("Sums Matrix:")
print(sums_matrix)

# Calculate the distribution of sums
sums_distribution = {}
for i in range(6):
    for j in range(6):
        sum_value = sums_matrix[i, j]
        if sum_value in sums_distribution:
            sums_distribution[sum_value] += 1
        else:
            sums_distribution[sum_value] = 1

print("Distribution of sums:")
for sum_value, count in sorted(sums_distribution.items()):
    print(f"Sum = {sum_value}: {count} occurrences")

# Part 3: Probability of All Possible Sums
# Calculate the probability of each sum as a fraction
probabilities = {}
for sum_value, count in sums_distribution.items():
    prob_fraction = Fraction(count, total_combinations)
    probabilities[sum_value] = prob_fraction

# Output
print("Probability of each sum (as fractions):")
for sum_value, prob in sorted(probabilities.items()):
    print(f"P(Sum = {sum_value}) = {prob}")
