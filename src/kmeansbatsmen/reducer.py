#!/usr/bin/env python
"""reducer.py"""

"""
This is the reducer file.
It gets sorted data from the mapper and calculates the new centroids file in the follwing manner:
    get centroid from input
    while centroid stays same, keep getting new centroids and summing up data while keeping count
    if centroid changes, calculate previous centroid, write to centroids file and start loop again
"""

import sys


def calculateNewCentroids():
    current_centroid = None
    sum_x = 0
    sum_y = 0
    count = 0

    for line in sys.stdin:

        # parse the input of mapper.py
        centroid_index, bname, x, y = line.split('\t')

        try:
            x = float(x)
            y = float(y)
        except ValueError:
            # float was not a number, so silently
            # ignore/discard this line
            continue

        # this IF-switch only works because Hadoop sorts map output
        # by key (here: word) before it is passed to the reducer
        if current_centroid == centroid_index:
            count += 1
            sum_x += x
            sum_y += y
        else:
            if count != 0:
                # print the average of every cluster to get new centroids
                print(str(sum_x / count) + ", " + str(sum_y / count))

            current_centroid = centroid_index
            sum_x = x
            sum_y = y
            count = 1

    # print last cluster's centroids
    if current_centroid == centroid_index and count != 0:
        print(str(sum_x / count) + ", " + str(sum_y / count))


if __name__ == "__main__":
    calculateNewCentroids()
