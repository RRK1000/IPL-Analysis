import sys
import csv
infile = sys.stdin

# distance based on (runs, balls)

fp = open("batsmandata.csv", "w+")
a = 0

for line in infile:
    if a == 1:
        data = line.split(",")
        if data[0][0] != "(":
            if data[4] == "-":
                if data[7] == "-":
                    fp.write(data[0] +",0,0\n")
                else:
                    fp.write(data[0] +",0," +data[7] +"\n")
            else:
                fp.write(data[0] +"," +data[4] +"," +data[7] +"\n")
    else:
        a = 1

fp.close()