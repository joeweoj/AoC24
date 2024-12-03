#!/usr/bin/env python3

import re, argparse

f = open("input.txt", "r")

total = 0
mul_matches, do_matches, dont_matches = [], [], []
toggle_locations = [{'start': 0, 'multiply': True}]

# Set up argument parser
parser = argparse.ArgumentParser()
parser.add_argument('-d', action='store_true', help='Enable debug mode')
args = parser.parse_args()

# Use the debug flag
def debug_print(msg):
    if args.d:
        print(msg)

# find the toggle preceding mul index
def should_multiply(mul_index):
    last_toggle = True
    for toggle in toggle_locations:
        debug_print(f"mul_index: {mul_index}, toggle: {toggle['start']}, multiply: {toggle['multiply']}")
        if mul_index < toggle['start']:
            debug_print(f"mul_index {mul_index} < toggle['start'] {toggle['start']} - breaking")
            break
        last_toggle = toggle['multiply']
    return last_toggle

# multiply if the toggle preceding mul index is True, otherwise 0
def multiply(x, y, mul_index):
    if should_multiply(mul_index):
        debug_print(f"multiplying {x} * {y} = {x * y}")
        return x * y
    else:
        debug_print(f"not multiplying {x} * {y} = 0")
        return 0

# get all multiplications, dos and don't matches
# ensure we're reading the entire file, otherwise do/don't/mul indices will be relative to line
while (line := f.read().strip()):
    mul_matches.extend(list(re.finditer(r'mul\(\d+,\d+\)', line)))
    do_matches.extend(list(re.finditer(r'do\(\)', line)))
    dont_matches.extend(list(re.finditer(r"don't\(\)", line)))

# sort dos and donts by start index
toggle_locations.extend({'start': m.start(), 'multiply': True} for m in do_matches)
toggle_locations.extend({'start': m.start(), 'multiply': False} for m in dont_matches)
toggle_locations = sorted(toggle_locations, key=lambda x: x['start'])

# iterate over multiplications, calculate and add to total
for match in mul_matches:
    operands = [int(x) for x in match.group().strip('mul(').strip(')').split(',')]
    total += multiply(operands[0], operands[1], match.start())


print(f'Total: {total}')