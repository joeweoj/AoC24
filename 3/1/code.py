#!/usr/bin/env python3

import re

f = open("input.txt", "r")

total = 0
while (line := f.readline().strip()):
    matches = re.findall(r'mul\(\d+,\d+\)', line)
    for match in matches:
        operands = [int(x) for x in match.strip('mul(').strip(')').split(',')]
        total += operands[0] * operands[1]
        print(f'{operands[0]} * {operands[1]} = {operands[0] * operands[1]}')


print(f'Total: {total}')