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

# read matrix into file
while (line := f.readline().strip()):
    wordsearch.append(list(line))
    debug_print(line)
debug_print('----------')

# test rows
total_found = 0
# this is frickin horrible, but gets the job done
for i, row in enumerate(wordsearch):
    for j, letter in enumerate(row):
        if letter == 'A':
            slash_count = 0
            try:
                if  i-1 >= 0 and j-1 >= 0 and \
                    wordsearch[i-1][j-1] == 'M' and \
                    wordsearch[i+1][j+1] == 'S':
                    debug_print(f'found MAS at {i}, {j} \\')
                    slash_count += 1
            except IndexError:
                pass
            try:
                if  i-1 >= 0 and j-1 >= 0 and \
                    wordsearch[i-1][j-1] == 'S' and \
                    wordsearch[i+1][j+1] == 'M':
                    debug_print(f'found SAM at {i}, {j} \\')
                    slash_count += 1
            except IndexError:
                pass
            try:
                if  i-1 >= 0 and j-1 >= 0 and \
                    wordsearch[i-1][j+1] == 'S' and \
                    wordsearch[i+1][j-1] == 'M':
                    debug_print(f'found SAM at {i}, {j} /')
                    slash_count += 1
            except IndexError:
                pass
            try:
                if  i-1 >= 0 and j-1 >= 0 and \
                    wordsearch[i-1][j+1] == 'M' and \
                    wordsearch[i+1][j-1] == 'S':
                    debug_print(f'found MAS at {i}, {j} /')
                    slash_count += 1
            except IndexError:
                pass
            if slash_count == 2:    
                total_found += 1
            else:
                debug_print(f'slash count {slash_count} at {i}, {j}')
print(total_found)
