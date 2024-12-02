#!/usr/bin/env python3

f = open("input.txt", "r")

# returns true if the report is safe, false otherwise
# note: O(n) on each report 3x which is bit meh
def is_safe(report_levels):
    safe_diff = is_safe_diff(report_levels)
    all_increasing = is_safe_increasing(report_levels)
    all_decreasing = is_safe_decreasing(report_levels)
    print(f'{report_levels}: is safe? {safe_diff and (all_increasing or all_decreasing)}. diff: {safe_diff}, increasing: {all_increasing}, decreasing: {all_decreasing})')
    return safe_diff and (all_increasing or all_decreasing)

# returns true if the diff between each level is between 1 and 3
def is_safe_diff(report_levels):
    for i in range(1, len(report_levels)):
        diff = abs(int(report_levels[i]) - int(report_levels[i - 1]))
        if diff > 3 or diff == 0:
            return False
    return True

# returns true if the report is strictly increasing
def is_safe_increasing(report_levels):
    return all(int(report_levels[i]) < int(report_levels[i + 1]) for i in range(len(report_levels) - 1))

# returns true if the report is strictly decreasing
def is_safe_decreasing(report_levels):
    return all(int(report_levels[i]) > int(report_levels[i + 1]) for i in range(len(report_levels) - 1))

# read the file line by line, and check if the report is safe
safe_reports = []
while (line := f.readline().strip()):
    report_levels = line.split()

    if is_safe(report_levels):
        safe_reports.append(report_levels)

print(f'Total safe reports: {len(safe_reports)}')