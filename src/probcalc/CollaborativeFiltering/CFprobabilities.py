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
        p0 = float(lines0[i].split(',')[2]) if float(lines0[i].split(',')[2]) > 0 else 0.0
        p1 = float(lines1[i].split(',')[2]) if float(lines1[i].split(',')[2]) > 0 else 0.0
        p2 = float(lines2[i].split(',')[2]) if float(lines2[i].split(',')[2]) > 0 else 0.0
        p3 = float(lines3[i].split(',')[2]) if float(lines3[i].split(',')[2]) > 0 else 0.0
        p4 = float(lines4[i].split(',')[2]) if float(lines4[i].split(',')[2]) > 0 else 0.0
        p5 = float(lines5[i].split(',')[2]) if float(lines5[i].split(',')[2]) > 0 else 0.0
        p6 = float(lines6[i].split(',')[2]) if float(lines6[i].split(',')[2]) > 0 else 0.0
        pw = float(linesw[i].split(',')[2]) if float(linesw[i].split(',')[2]) > 0 else 0.0

        batsman = lines0[i].split(',')[0]
        bowler = lines0[i].split(',')[1]

        probdict = [p0,p1,p2,p3,p4,p5,p6]
        for i in range(6):
            try:
                probdict[i] = probdict[i]/sum(probdict)
            except ZeroDivisionError: #NEEDS TO BE CHANGED
                print(batsman, bowler, sep=", ")
                probdict[i] = 1.0/6
        probdict[6] = 1 - sum(probdict[:6])

        finalProb[(batsman, bowler)] = dict()
        for i in range(7):
            finalProb[(batsman, bowler)][i] = probdict[i]
        finalProb[(batsman, bowler)]["W"] = pw


    d0.close()
    d1.close()
    d2.close()
    d3.close()
    d4.close()
    d5.close()
    d6.close()
    dw.close()

    return finalProb

prob = CFprobabilities()
# for key in prob.keys():
#     print(key, prob[key])