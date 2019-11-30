"""
This file is used to calculate the difference between the newly generated centroids and the
previous centroids and return a flag to signify if the centroids have stayed constant
"""

from mapper import getCentroids

# check if distance of centroids and centroids1 is less than 1


def checkCentroidsDistance(centroids, centroids1):
    i = 0
    fl = False
    try:
        while(1):
            f1x = abs(centroids[i][0] - centroids1[i][0]) < 1
            f1y = abs(centroids[i][1] - centroids1[i][1]) < 1
            # f2x = abs(centroids[1][0] - centroids1[1][0])<1
            # f2y = abs(centroids[1][1] - centroids1[1][1])<1
            # f3x = abs(centroids[2][0] - centroids1[2][0])<1
            # f3y = abs(centroids[2][1] - centroids1[2][1])<1

            fl = f1x and f1y
            if not fl:
                print(0)
                break
            i += 1
    except IndexError:
        if fl:
            print(1)
        else:
            print(0)

    # if f1x and f1y and f2x and f2y and f3x and f3y:
    #     print(1)
    # else:
    #     print(0)


if __name__ == "__main__":
    centroids = getCentroids('centroids.txt')
    centroids1 = getCentroids('centroids1.txt')

    checkCentroidsDistance(centroids, centroids1)
