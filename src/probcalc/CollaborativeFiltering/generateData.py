data = open("../../../data/alldata2017.csv", "r")
d0 = open("./data/p0.csv", "w")
d1 = open("./data/p1.csv", "w")
d2 = open("./data/p2.csv", "w")
d3 = open("./data/p3.csv", "w")
d4 = open("./data/p4.csv", "w")
d5 = open("./data/p5.csv", "w")
d6 = open("./data/p6.csv", "w")
dw = open("./data/pw.csv", "w")

prob = {}

for line in data.readlines():
    line = line.split(',')
    if((line[4],line[6]) not in prob):
        prob[(line[4],line[6])] = {0: 0, 1: 0, 2: 0, 3: 0,
                              4: 0, 5: 0, 6: 0, "W": 0, "B": 0}

    if line[0] == "ball":
        batsman = line[4]
        bowler = line[6]

        try:
            if line[10]:
                prob[(line[4],line[6])]["W"] +=1
        except IndexError:
            runs = int(line[7])
            prob[(line[4],line[6])][runs] +=1

        prob[(line[4],line[6])]["B"] +=1

for key in prob.keys():
    d0.write(str(key[0])+','+str(key[1])+',' + str(float(prob[key][0])/float(prob[key]["B"]))+'\n')
    d1.write(str(key[0])+','+str(key[1])+',' + str(float(prob[key][1])/float(prob[key]["B"]))+'\n')
    d2.write(str(key[0])+','+str(key[1])+',' + str(float(prob[key][2])/float(prob[key]["B"]))+'\n')
    d3.write(str(key[0])+','+str(key[1])+',' + str(float(prob[key][3])/float(prob[key]["B"]))+'\n')
    d4.write(str(key[0])+','+str(key[1])+',' + str(float(prob[key][4])/float(prob[key]["B"]))+'\n')
    d5.write(str(key[0])+','+str(key[1])+',' + str(float(prob[key][5])/float(prob[key]["B"]))+'\n')
    d6.write(str(key[0])+','+str(key[1])+',' + str(float(prob[key][6])/float(prob[key]["B"]))+'\n')
    dw.write(str(key[0])+','+str(key[1])+',' + str(float(prob[key]["W"])/float(prob[key]["B"]))+'\n')

d0.close()
d1.close()
d2.close()
d3.close()
d4.close()
d5.close()
d6.close()
dw.close()