fd = open("bowlerdata.csv", "r")
new = open("centroids.txt", "w+")

maxa = 0
maxb = 0
count = 0

for line in fd.readlines():
    line = line.split(",")
    for i in range(1, 3):
        line[i] = int(float(line[i].rstrip("\n")))
    if line[1] > maxa:
        maxa = line[1]
    if line[2] > maxb:
        maxb = line[2]
    count += 1

k = 5
amultiple = maxa/k
bmultiple = maxb/k
for i in range(1, int(k)):
    new.write(str(amultiple*i) + ", " + str(bmultiple*i) + "\n")

fd.close()
new.close()
