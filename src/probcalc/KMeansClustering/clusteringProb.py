import time

def getKMeansClusters():
    data = open("../../data/alldata2017.csv", "r")
    batsmanData = open("../../batsmanKMeansOutput.txt", "r")
    bowlerData = open("../../bowlerKMeansOutput.txt", "r")

    batsmenclusters = dict()
    bowlerclusters = dict()
    batsmenclusterset = set()
    bowlerclusterset = set()
    finalprobs = dict()

    for line in batsmanData.readlines():
        line = line.split("\t")
        batsmenclusters[line[1]] = int(line[0])
        batsmenclusterset.add(int(line[0]))

    for line in bowlerData.readlines():
        line = line.split("\t")
        bowlerclusters[line[1]] = int(line[0])
        bowlerclusterset.add(int(line[0]))


    for i in batsmenclusterset:
        for j in bowlerclusterset:
            finalprobs[(i, j)] = {0: 0.0, 1: 0.0, 2: 0.0, 3: 0.0,
                                4: 0.0, 5: 0.0, 6: 0.0, "W": 0.0, "B": 0.0}


    for line in data.readlines():
        line = line.split(",")

        if line[0] == "ball":
            batsman = line[4]
            bowler = line[6]

            try:
                if line[10]:
                    finalprobs[(batsmenclusters[batsman], bowlerclusters[bowler])]["W"] = finalprobs[(
                        batsmenclusters[batsman], bowlerclusters[bowler])]["W"] + 1.0
            except IndexError:
                runs = int(line[7])
                finalprobs[(batsmenclusters[batsman], bowlerclusters[bowler])][runs] = finalprobs[(
                    batsmenclusters[batsman], bowlerclusters[bowler])][runs] + 1.0

            finalprobs[(batsmenclusters[batsman], bowlerclusters[bowler])]["B"] = finalprobs[(
                batsmenclusters[batsman], bowlerclusters[bowler])]["B"] + 1.0

    probs = dict()
    for batsman in batsmenclusters.keys():
        for bowler in bowlerclusters.keys():
            if batsman!=bowler:
                probs[(batsman,bowler)] = finalprobs[(batsmenclusters[batsman]), bowlerclusters[bowler]].copy()
    
    for key in probs.keys():
        for i in range(7):
            probs[key][i] = probs[key][i]/probs[key]["B"]
        
        sumprobs = 0.0
        for i in range(7):
            sumprobs += probs[key][i]
        for i in range(7):
            probs[key][i] = probs[key][i]/sumprobs
        
        newsum = 0
        for i in range(6):
            newsum += probs[key][i]
        probs[key][7] = 1 - newsum
        newsum += probs[key][7]

        probs[key]["W"] = probs[key]["W"]/probs[key]["B"]
        # print(newsum)
        
    return probs

# getKMeansClusters()