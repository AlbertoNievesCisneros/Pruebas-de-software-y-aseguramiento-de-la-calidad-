#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import sys
import time

def read_numbers_from_file(file_path):
    numbers = []
    with open(file_path, 'r') as file:
        for line in file:
            try:
                number = float(line.strip())
                numbers.append(number)
            except ValueError:
                print(f"Invalid data: {line.strip()}")
    return numbers

def mean(numbers):
    return sum(numbers) / len(numbers)

def median(numbers):
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2
    else:
        return sorted_numbers[mid]

def mode(numbers):
    frequency = {}
    for number in numbers:
        frequency[number] = frequency.get(number, 0) + 1
    max_frequency = max(frequency.values())
    modes = [key for key, val in frequency.items() if val == max_frequency]
    return modes[0] if len(modes) == 1 else modes

def variance(numbers, mean_value):
    return sum((x - mean_value) ** 2 for x in numbers) / len(numbers)

def standard_deviation(variance_value):
    return variance_value ** 0.5

def write_results_to_file(results, file_name):
    with open(file_name, 'w') as file:
        for key, value in results.items():
            file.write(f"{key}: {value}\n")

def main(file_path):
    start_time = time.time()
    numbers = read_numbers_from_file(file_path)
    if numbers:
        results = {
            'Mean': mean(numbers),
            'Median': median(numbers),
            'Mode': mode(numbers),
            'Variance': variance(numbers, mean(numbers)),
            'Standard Deviation': standard_deviation(variance(numbers, mean(numbers)))
        }

        for key, value in results.items():
            print(f"{key}: {value}")

        write_results_to_file(results, 'StatisticsResults.txt')
        elapsed_time = time.time() - start_time
        print(f"Time elapsed: {elapsed_time} seconds")
        with open('StatisticsResults.txt', 'a') as file:
            file.write(f"Time elapsed: {elapsed_time} seconds\n")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python computeStatistics.py fileWithData.txt")
        sys.exit(1)
    main(sys.argv[1])

