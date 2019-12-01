import random
from CumulativeProb import CP
from CFprobabilities import *
import math
import sys


def CalculateRuns(r, batsman_1, bowler, cumulative_prob):
    run = 0
    while run <= 6 and (cumulative_prob[(batsman_1, bowler)][run] < r) :
        run+=1
    
    return run


bowlerOrder = ["AB Dinda", "BA Stokes", "AB Dinda", "Imran Tahir", "A Zampa", "BA Stokes", "AB Dinda", "R Bhatia", "DL Chahar", "BA Stokes", "AB Dinda", "Imran Tahir", "A Zampa", "BA Stokes", "AB Dinda", "R Bhatia", "DL Chahar", "BA Stokes", "DL Chahar", "A Zampa"]
batsmanOrder = ["PA Patel", "JC Buttler", "RG Sharma", "N Rana", "AT Rayudu", "KH Pandya", "KA Pollard", "HH Pandya", "TG Southee", "MJ McClenaghan", "JJ Bumrah"]

# data = open("batsbowlorder.csv", "r")

# for line in data.readlines():
#     line = line.split("\t")
#     batsmanOrder.append(line[0])
#     bowlerOrder.append(line[1])

cumulative_prob = CP()
cf_prob = CFprobabilities()
print(cumulative_prob[('PA Patel', 'BA Stokes')])

# numberOfBalls = 0
# wickets = 0
# score = 0
# ball_score = 0
# overs = 0
# b = 0                                   # Ball in over

# batsman_1 = batsmanOrder[0]             # On-Strike Batsman
# batsman_2 = batsmanOrder[1]             # Off-Strike Batsman
# bowler = bowlerOrder[0].rstrip("\n")    # First Bowler
# bowler_index = 0                        # Index of next bowler
# batting_index = 1                       # Index of next batsman

# # Initial wicket probabilities
# wicket_prob = {(batsman_1, bowler): 1 - cf_prob[(
#     batsman_1, bowler)]["W"], (batsman_2, bowler): 1 - cf_prob[(batsman_2, bowler)]["W"]}

# while(wickets <= 10 and numberOfBalls <= 120):
#     b += 1
#     numberOfBalls += 1
#     # Updating wicket probability
#     if (batsman_1, bowler) not in wicket_prob:
#         wicket_prob[(batsman_1, bowler)] = 1 - cf_prob[(batsman_1, bowler)]["W"]
#     else:
#         tmp = wicket_prob[(batsman_1, bowler)]
#         wicket_prob[(batsman_1, bowler)] = tmp * (1 - cf_prob[(batsman_1, bowler)]["W"])
#     if(wicket_prob[(batsman_1, bowler)] < 0.7):
#         wickets += 1
#         batting_index += 1
#         batsman_1 = batsmanOrder[batting_index]
#         ball_score = 0
#         print("Wicket:", batsman_1)
#     else:
#         r = random.uniform(0.1, 0.9999)  
#         ball_score = CalculateRuns(r, batsman_1, bowler, cumulative_prob)

#     score += ball_score
#     print("Score : %d/%d" % (score, wickets))

#     # End of Over    
#     if(b == 7 and numberOfBalls<=120):
#         batsman_1, batsman_2 = batsman_2, batsman_1
#         bowler_index += 1
#         bowler = bowlerOrder[bowler_index].rstrip("\n")
#         b = 1
#         overs +=1
