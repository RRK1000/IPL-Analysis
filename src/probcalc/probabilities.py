data = open("../../data/alldata2017.csv", "r")
badata = open("../batsmanKMeansOutput.txt", "r")
bodata = open("../bowlerKMeansOutput.txt", "r")

batsmenclusters = dict()
bowlerclusters = dict()
batsmenclusterset = set()
bowlerclusterset = set()
finalprobs = dict()

for line in badata.readlines():
    line = line.split("\t")
    batsmenclusters[line[1]] = int(line[0])
    batsmenclusterset.add(int(line[0]))

for line in bodata.readlines():
    line = line.split("\t")
    bowlerclusters[line[1]] = int(line[0])
    bowlerclusterset.add(int(line[0]))


for i in batsmenclusterset:
    for j in bowlerclusterset:
        finalprobs[(i,j)] = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, "W":0, "B":0}


for line in data.readlines():
    line = line.split(",")

    if line[0] == "ball":
        print(line)
        batsman = line[4]
        bowler = line[6]
        
        try:
            if line[10]:
                finalprobs[(batsmenclusters[batsman],bowlerclusters[bowler])]["W"] = finalprobs[(batsmenclusters[batsman],bowlerclusters[bowler])]["W"] + 1
        except IndexError:
            runs = int(line[7])
            finalprobs[(batsmenclusters[batsman],bowlerclusters[bowler])][runs] = finalprobs[(batsmenclusters[batsman],bowlerclusters[bowler])][runs] + 1
        
        finalprobs[(batsmenclusters[batsman],bowlerclusters[bowler])]["B"] = finalprobs[(batsmenclusters[batsman],bowlerclusters[bowler])]["B"] + 1

for key in finalprobs.keys():
    print(key, finalprobs[key])