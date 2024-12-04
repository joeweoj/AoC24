#!/usr/bin/env python3

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-d', action='store_true', help='Enable debug output')
parser.add_argument('file', help='Path to input file')  # Add this line
args = parser.parse_args()

wordsearch = []

f = open(args.file, 'r')


def debug_print(msg):
    if args.d:
        print(msg)

# given array of chars, look for 'xmas' back/forwards
def test_chars(chars):
    found_count = 0
    for j in range(len(chars)):
        fwd_test = chars[j:j+4]
        if ''.join(fwd_test) == 'XMAS':
            found_count += 1

        # backwards
        bwd_test = chars[j-3:j+1]   
        if ''.join(bwd_test) == 'XMAS'[::-1]:
            found_count += 1
    return found_count

# read matrix into file
while (line := f.readline().strip()):
    wordsearch.append(list(line))
    debug_print(line)
debug_print('----------')

# test rows
total_found = 0
for i, row in enumerate(wordsearch):
    debug_print(f'testing row {i}: {row}')
    total_found += test_chars(row)

# test columns
for j, letter in enumerate(wordsearch[0]):
    column = [row[j] for row in wordsearch]
    debug_print(f'testing column {j}: {column}')
    total_found += test_chars(column)

# this is frickin horrible, but gets the job done
for i, row in enumerate(wordsearch):
    for j, letter in enumerate(row):
        try:
            if  i-3 >= 0 and j-3 >= 0 and \
                wordsearch[i][j] == 'X' and \
                wordsearch[i-1][j-1] == 'M' and \
                wordsearch[i-2][j-2] == 'A' and \
                wordsearch[i-3][j-3] == 'S':
                debug_print(f'found XMAS at {i}, {j} up,left')
                total_found += 1
        except IndexError:
            pass
        try:
            if  wordsearch[i][j] == 'X' and \
                wordsearch[i+1][j+1] == 'M' and \
                wordsearch[i+2][j+2] == 'A' and \
                wordsearch[i+3][j+3] == 'S':
                debug_print(f'found XMAS at {i}, {j} down,right')
                total_found += 1
        except IndexError:
            pass

        try:
            if  j-3 >= 0 and \
                wordsearch[i][j] == 'X' and \
                wordsearch[i+1][j-1] == 'M' and \
                wordsearch[i+2][j-2] == 'A' and \
                wordsearch[i+3][j-3] == 'S':
                debug_print(f'found XMAS at {i}, {j} down, left')
                total_found += 1
        except IndexError:
            pass

        try:
            if  i-3 >= 0 and \
                wordsearch[i][j] == 'X' and \
                wordsearch[i-1][j+1] == 'M' and \
                wordsearch[i-2][j+2] == 'A' and \
                wordsearch[i-3][j+3] == 'S':
                debug_print(f'found XMAS at {i}, {j} up,right')
                total_found += 1
        except IndexError:
            pass


print(total_found)


   