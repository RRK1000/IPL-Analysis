import sys
import csv
infile = sys.stdin

# distance based on (average, strike rate)

fp = open("../src/kmeansbatsmen/batsmandata.csv", "w+")
a = 0

for line in infile:
    if a == 1:
        data = line.split(",")
        if data[0][0] != "(":
            if data[8] != "-":
                if data[6] == "-":
                    fp.write(data[0] +",0," +data[8] +"\n")
                else:
                    fp.write(data[0] +"," +data[6] +"," +data[8] +"\n")
            else:
                if data[6] == "-":
                    fp.write(data[0] +",0,0\n")
                else:
                    fp.write(data[0] +"," +data[6] +",\n")
    else:
        a = 1

fp.close()
