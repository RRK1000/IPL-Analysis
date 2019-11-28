import sys
import csv
infile = sys.stdin

# distance based on (wickets, econ)

fp = open("bowlerdata.csv", "w+")
a = 0

for line in infile:
    if a == 1:
        data = line.split(",")
        if data[0][0] != "(":
            if data[9] != "-":
                if data[6] == "-":
                    fp.write(data[0] +",0," + data[9]+"\n")
                else:
                    fp.write(data[0] +"," +data[6] +","+data[9]+"\n")
            else:
                if data[6]=="-":
                    fp.write(data[0] +",0,0\n")
                else:
                    fp.write(data[0]+","+data[6]+"\n")
    else:
        a = 1

fp.close()