data = open("../../data/alldata.csv", "r")
clusterdata = open("../batsmanKMeansOutput.txt", "r")

clusters = {}

for line in clusterdata.readlines():
    line = line.split("\t")
    