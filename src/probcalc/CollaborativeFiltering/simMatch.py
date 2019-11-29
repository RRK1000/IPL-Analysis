import random
from generateProbabilities import *

# def CalculateRuns(r, probabilities, cur_bats1, cur_bowl):

bowlerOrder = []
batsmanOrder = []

numberOfBalls = 0
wickets = 0
score = 0
b = 0 #ball in over

cur_bats1 = batsmanOrder[0]	#The batsman facing the bowler
cur_bats2 = batsmanOrder[1]	
batting_index = 1
cur_bowl = bowlerOrder[0]
bowler_index = 0

probabilities = generateProbabilities()

while(wickets<=10 and numberOfBalls<=120):
    r = random.randint(0,1)
    result = CalculateRuns(r, probabilities, cur_bats1, cur_bowl)
    if(b >= 6):		#End of over
        cur_bats1, cur_bats2 = cur_bats2, cur_bats1
        bowler_index += bowler_index
        cur_bowl = bowlerOrder[bowler_index]
        b = 0

    if(result == -1):
        wickets += 1
        numberOfBalls += 1
        bowler_index +=1
        cur_bats2 = cur_bats1
        cur_bats1 = batsmanOrder[bowler_index]

    elif(result == 1):
        numberOfBalls += 1
        score += result
        cur_bats1, cur_bats2 = cur_bats2, cur_bats1

    elif(result == 2):
        numberOfBalls += 1
        score += result

    elif(result == 3):
        numberOfBalls += 1
        score += result
        cur_bats1, cur_bats2 = cur_bats2, cur_bats1

    elif(result == 4):
        numberOfBalls += 1
        score += result

    elif(result == 5):
        numberOfBalls += 1
        score += result
        cur_bats1, cur_bats2 = cur_bats2, cur_bats1
    
    elif(result == 6):
        numberOfBalls += 1
        score += result





