#!/usr/bin/env python3

f = open("input.txt", "r")

# read input and append location ids to L, R arrays
left = []
right = []
while (line := f.readline().strip()):
    locationIds = line.split()
    left.append(int(locationIds[0]))
    right.append(int(locationIds[1]))

# sort L & R arrays
left.sort()
right.sort()

assert len(left) == len(right)

# find 'distance' between L[n] and R[n]
# add to total distance
distances = []
total_distance = 0
for i in range(len(left)):
    distance = abs(left[i] - right[i])
    total_distance += distance
    distances.append(distance)
    print(f'{left[i]} {right[i]} {distance}')

print('total distance:', total_distance)