import sys
import csv
infile = sys.stdin

# distance based on (wickets, balls)

fp = open("bowlerdata.csv", "w+")
a = 0

for line in infile:
    if a == 1:
        data = line.split(",")
        if data[0][0] != "(":
            if data[3] != "-":
                overs = data[3]
                overs = float(overs)
                ext = int(overs*10%10)
                overs = int(overs)
            else:
                overs = 0
                ext = 0
            
            balls = overs*6 + ext

            if data[6] == "-":
                fp.write(data[0] +",0," +str(balls) +",1\n")
            else:
                fp.write(data[0] +"," +data[6] +"," +str(balls) +",1\n")
    else:
        a = 1

fp.close()