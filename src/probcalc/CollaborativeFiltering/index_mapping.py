data = open("./data/p0.csv", "r")
bat = open("./data/batsman_index.csv", "w")
bowl = open("./data/bowler_index.csv", "w")
batsmen = {}
b1 = {}
batsmen_index = 0
bowlers = {}
b2 = {}
bowlers_index =0

for line in data.readlines():
    line = line.split(',')
    if(line[0] not in batsmen.values()):
        batsmen[batsmen_index] = line[0]
        # b1[line[0]] = batsmen_index
        bat.write(line[0]+ ',' + str(batsmen_index) + '\n')
        batsmen_index+=1

    if(line[1] not in bowlers.values()):
        bowlers[bowlers_index] = line[1]
        # b2[line[1]] = bowlers_index
        bowl.write(line[1]+ ',' + str(bowlers_index) + '\n')
        bowlers_index+=1


bat.close()
bowl.close()