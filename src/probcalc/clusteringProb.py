data = open("../../data/alldata2017.csv", "r")
batsmanData = open("../batsmanKMeansOutput.txt", "r")
bowlerData = open("../bowlerKMeansOutput.txt", "r")
fp = open("clusteringProbabilities.csv", "w")

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
        finalprobs[(i, j)] = {0: 0, 1: 0, 2: 0, 3: 0,
                              4: 0, 5: 0, 6: 0, "W": 0, "B": 0}


for line in data.readlines():
    line = line.split(",")

    if line[0] == "ball":
        batsman = line[4]
        bowler = line[6]

        try:
            if line[10]:
                finalprobs[(batsmenclusters[batsman], bowlerclusters[bowler])]["W"] = finalprobs[(
                    batsmenclusters[batsman], bowlerclusters[bowler])]["W"] + 1
        except IndexError:
            runs = int(line[7])
            finalprobs[(batsmenclusters[batsman], bowlerclusters[bowler])][runs] = finalprobs[(
                batsmenclusters[batsman], bowlerclusters[bowler])][runs] + 1

        finalprobs[(batsmenclusters[batsman], bowlerclusters[bowler])]["B"] = finalprobs[(
            batsmenclusters[batsman], bowlerclusters[bowler])]["B"] + 1

# for key in finalprobs.keys():
#     fp.write(str(key[0])+','+str(key[1])+',' + str(float(finalprobs[key][0])/float(finalprobs[key]["B"]))+',' + str(float(finalprobs[key][1])/float(finalprobs[key]["B"]))+',' + str(float(finalprobs[key][2])/float(finalprobs[key]["B"]))+',' + str(float(finalprobs[key][3])/float(
#         finalprobs[key]["B"]))+',' + str(float(finalprobs[key][4])/float(finalprobs[key]["B"])) + ',' + str(float(finalprobs[key][5])/float(finalprobs[key]["B"])) + ',' + str(float(finalprobs[key][6])/float(finalprobs[key]["B"])) + ',' + str(float(finalprobs[key]["W"])/float(finalprobs[key]["B"])) + '\n')

probs = dict()
for batsman in batsmenclusters.keys():
    for bowler in bowlerclusters.keys():
        probs[(batsman,bowler)] = finalprobs[(batsmenclusters[batsman]), bowlerclusters[bowler]]

for key in probs.keys():
    print(key, probs[key])