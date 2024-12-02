# Assumes that input.txt exists and has the input

# Solution: (Part One)
## We can read all the lines of the file and put the values into two different arrays
## After which we can sort the arrays, and compare elements accordingly
## And finally return the distances

import re
from typing import List

with open("./input.txt", "r") as inp_file:
    list1: List[int] = []
    list2: List[int] = []
    dist: int = 0

    # Taking in the input
    input_txt = inp_file.read()
    # setting values accordingly
    lines: List[str] = input_txt.split("\n")

    for line in lines:
        # Y'all really don't have a built in way to handle regex w/o a package huh? 💀
        # I just would use / +/ to separate w/ multiple whitespaces in b/w the two numbers wtf
        # [elem1, elem2] = lines.split(/ +/)
        [elem1, elem2] = re.split("\s+", line)
        list1.append(int(elem1))
        list2.append(int(elem2))

    # Sorting the lists
    list1.sort()
    list2.sort()

    # Comparing the lists
    for i in range(0, len(list1)):
        point_dist: int = abs(list1[i] - list2[i])
        dist += point_dist
        print(f"Distance: currently at index {i} with a diff {point_dist}")

    print(f"The distance between the lists is: {dist}")
    # This is the solution to the first part of the problem

# Solution: (Part Two)

## One way to compare the two arrays would be to have moving pointers
## So we move the left pointer in increments and move the right pointer as we find value at right pointer being less than value at left pointer, adding to sim_score if there is a value at right that's equal to the value in consideration

    r_ptr: int = 0
    sim_score: int = 0

    # Could I have done this in the previous loop? Yes
    # But it kinda ruins the segregation aspect of the code, that part 1 and part 2 as separate kinda thing
    for i in range(0, len(list1)):
        print(f"Sim Score: currently at index {i} with sim score {sim_score}")
        if list2[r_ptr] > list1[i]:
            continue # Anyways the sim_score for this elem is 0

        while list2[r_ptr] < list1[i]:
            r_ptr += 1

        # Calculating sim_count of iteration
        sim_count: int = 0
        while list2[r_ptr] == list1[i]:
            r_ptr += 1
            sim_count += 1

        sim_score += sim_count * list1[i]

        # Resetting r_ptr as it is possible that there are multiple elements of same value in list1, and they all add to the sim_score
        r_ptr -= sim_count

    print(f"The similarity score of the two lists is: {sim_score}")
