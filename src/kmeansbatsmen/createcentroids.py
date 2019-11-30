'''
This file is used to generate initial centroids

The way this is being done is that the max of each feature is taken and there are
k centroids being places equidistant starting from (0,0) till (maxa, maxb)
'''

fd = open("batsmandata.csv", "r")
new = open("centroids.txt", "w+")

maxa = 0
maxb = 0
count = 0

#finding maximum of each feature
for line in fd.readlines():
    line = line.split(",")
    for i in [1,2]:
        line[i] = float(line[i])
    if line[1] > maxa:
        maxa = line[1]
    if line[2] > maxb:
        maxb = line[2]
    count += 1

k = 5
amultiple = maxa/k
bmultiple = maxb/k

#creating equidistant centroids
for i in range(1, int(k)):
    new.write(str(amultiple*i) + ", " + str(bmultiple*i) + "\n")

fd.close()
new.close()
