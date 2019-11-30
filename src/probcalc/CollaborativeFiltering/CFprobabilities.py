def CFprobabilities():
    d0 = open("./data/p0_pred.csv", "r")
    d1 = open("./data/p1_pred.csv", "r")
    d2 = open("./data/p2_pred.csv", "r")
    d3 = open("./data/p3_pred.csv", "r")
    d4 = open("./data/p4_pred.csv", "r")
    d5 = open("./data/p5_pred.csv", "r")
    d6 = open("./data/p6_pred.csv", "r")
    dw = open("./data/pw_pred.csv", "r")

    lines0 = d0.readlines()
    lines1 = d1.readlines()
    lines2 = d2.readlines()
    lines3 = d3.readlines()
    lines4 = d4.readlines()
    lines5 = d5.readlines()
    lines6 = d6.readlines()
    linesw = dw.readlines()

    length = len(lines0)-1
    finalProb = {}
    for i in range(length):
        batsman = lines0[i].split(',')[0]
        bowler = lines0[i].split(',')[1]
        finalProb[(batsman, bowler)] = {0: abs(float(lines0[i].split(',')[2])), 1: abs(float(lines1[i].split(',')[2])), 2: abs(float(lines2[i].split(',')[2])), 3: abs(float(lines3[i].split(
            ',')[2])), 4: abs(float(lines4[i].split(',')[2])), 5: abs(float(lines5[i].split(',')[2])), 6: abs(float(lines6[i].split(',')[2])), "W": abs(float(linesw[i].split(',')[2]))}

    d0.close()
    d1.close()
    d2.close()
    d3.close()
    d4.close()
    d5.close()
    d6.close()
    dw.close()

    return finalProb

# prob = CFprobabilities()
# for i in prob.items():
#     print(i)