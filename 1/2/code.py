#!/usr/bin/env python3

f = open("input.txt", "r")

# read input and append location ids to L, R arrays
left = []
right = {}
while (line := f.readline().strip()):
    locationIds = line.split()
    l_loc_id = int(locationIds[0])
    r_loc_id = int(locationIds[1])
    left.append(l_loc_id)
    # keep counter of how many times each R location id appears
    right[r_loc_id] = right.get(r_loc_id, 0) + 1
    
total_similarity_score = 0
for l_loc_id in left:
    # lookup number of times l_loc_id appears in right
    r_loc_count = right.get(l_loc_id, 0)
    print(f'{l_loc_id} appears in R list {r_loc_count} times. {l_loc_id} * {r_loc_count} = {l_loc_id * r_loc_count}')
    total_similarity_score += l_loc_id * r_loc_count

print('total similarity score:', total_similarity_score)