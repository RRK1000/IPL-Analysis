import random

from CumulativeProb import CP
from clusteringProb import getKMeansClusters
import math


def CalculateRuns(r, batsman_1, bowler, cumulative_prob):
    run = 0
    while run<=6 and cumulative_prob[(batsman_1, bowler)][run] <= r:
        run+=1
    
    return run


def Innings1():
	'''bowlerOrder = ["Q de Kock","UT Yadav","V Kohli","AB de Villiers","P Negi","UT Yadav","CJ Anderson","C de Grandhomme","Mohammed Siraj","Mandeep Singh","C de Grandhomme","P Negi","V Kohli","CJ Anderson","Washington Sundar","UT Yadav","Mohammed Siraj","YS Chahal","Q de Kock","P Negi"]
	batsmanOrder = ["SR Watson","AT Rayudu","SK Raina","SW Billings","RA Jadeja","MS Dhoni","DJ Bravo","Harbhajan Singh","DL Chahar","SN Thakur","Imran Tahir"]'''
	bowlerOrder = []
	batsmanOrder = []

	data = open("Team1bats.csv", "r")
	for line in data.readlines():
    		batsmanOrder.append(line)
	

	data = open("Team2bowl.csv", "r")
	for line in data.readlines():
    		bowlerOrder.append(line)
	

	cumulative_prob = CP()
	clustering_prob = getKMeansClusters()

	numberOfBalls = 0
	wickets = 0
	score = 0
	ball_score = 0
	overs = 0
	b = 0                                  # Ball in over
	

	batsman_1 = batsmanOrder[0].rstrip("\n")             # On-Strike Batsman
	batsman_2 = batsmanOrder[1].rstrip("\n")             # Off-Strike Batsman
	bowler = bowlerOrder[0].rstrip("\n")    # First Bowler
	bowler_index = 0                        # Index of next bowler
	batting_index = 1                       # Index of next batsman

	# Initial wicket probabilities
	wicket_prob = {(batsman_1, bowler): 1 - clustering_prob[(
    	batsman_1, bowler)]["W"], (batsman_2, bowler): 1 - clustering_prob[(batsman_2, bowler)]["W"]}

	while(wickets <= 10 and numberOfBalls < 120):
    		b += 1
    		numberOfBalls += 1
    		# Updating wicket probability
    		if (batsman_1, bowler) not in wicket_prob:
        		wicket_prob[(batsman_1, bowler)] = 1 - clustering_prob[(batsman_1, bowler)]["W"]
    		else:
        		tmp = wicket_prob[(batsman_1, bowler)]
        		wicket_prob[(batsman_1, bowler)] = tmp * (1 - clustering_prob[(batsman_1, bowler)]["W"])
    		if(wicket_prob[(batsman_1, bowler)] < 0.7):
        		print("%d.%d\t%s\t%s\tW" % (overs,b,batsman_1,bowler))
        		
        		wickets += 1
        		batting_index += 1
        		batsman_1 = batsmanOrder[batting_index].rstrip("\n")
        		ball_score = 0
    		else:
        		r = random.uniform(0.1, 0.9999)  
        		ball_score = CalculateRuns(r, batsman_1, bowler, cumulative_prob)
        		print("%d.%d\t%s\t%s\t%d" % (overs,b,batsman_1,bowler,ball_score))
        		
    		score += ball_score

    		if(ball_score%2):
        		batsman_1, batsman_2 = batsman_2, batsman_1

    		# End of Over    
    		if(b == 6 and numberOfBalls<120):
        		batsman_1, batsman_2 = batsman_2, batsman_1
        		bowler_index += 1
        		bowler = bowlerOrder[bowler_index].rstrip("\n")
        		b = 0
        		overs +=1
	print("Target =", score+1)	
	return score

def Innings2(Target):
	'''batsmanOrder = ["Q de Kock","V Kohli","AB de Villiers","CJ Anderson","Mandeep Singh","C de Grandhomme","P Negi","Washington Sundar","UT Yadav","Mohammed Siraj","YS Chahal"]
	bowlerOrder = ["SR Watson","MS Dhoni","AT Rayudu","SK Raina","SW Billings","RA Jadeja","SW Billings","DJ Bravo","Harbhajan Singh","MS Dhoni","SR Watson","DJ Bravo","Harbhajan Singh","AT Rayudu","DL Chahar","SN Thakur","AT Rayudu","Imran Tahir","MS Dhoni","SW Billings"]'''

	bowlerOrder = []
	batsmanOrder = []

	data = open("Team2bats.csv", "r")
	for line in data.readlines():
    		batsmanOrder.append(line)

	data = open("Team1bowl.csv", "r")
	for line in data.readlines():
    		bowlerOrder.append(line)

	cumulative_prob = CP()
	clustering_prob = getKMeansClusters()

	numberOfBalls = 0
	wickets = 0
	score = 0
	ball_score = 0
	overs = 0
	b = 0                                   # Ball in over
	

	batsman_1 = batsmanOrder[0].rstrip("\n")             # On-Strike Batsman
	batsman_2 = batsmanOrder[1].rstrip("\n")             # Off-Strike Batsman
	bowler = bowlerOrder[0].rstrip("\n")    # First Bowler
	bowler_index = 0                        # Index of next bowler
	batting_index = 1                       # Index of next batsman

	# Initial wicket probabilities
	wicket_prob = {(batsman_1, bowler): 1 - clustering_prob[(
    	batsman_1, bowler)]["W"], (batsman_2, bowler): 1 - clustering_prob[(batsman_2, bowler)]["W"]}

	while(wickets <= 10 and numberOfBalls < 120 and score<=Target):
    		b += 1
    		numberOfBalls += 1
    		# Updating wicket probability
    		if (batsman_1, bowler) not in wicket_prob:
        		wicket_prob[(batsman_1, bowler)] = 1 - clustering_prob[(batsman_1, bowler)]["W"]
    		else:
        		tmp = wicket_prob[(batsman_1, bowler)]
        		wicket_prob[(batsman_1, bowler)] = tmp * (1 - clustering_prob[(batsman_1, bowler)]["W"])
    		if(wicket_prob[(batsman_1, bowler)] < 0.7):
        		print("%d.%d\t%s\t%s\tW" % (overs,b,batsman_1,bowler))
        		
        		wickets += 1
        		batting_index += 1
        		batsman_1 = batsmanOrder[batting_index].rstrip("\n")
        		ball_score = 0
    		else:
        		r = random.uniform(0.1, 0.9999)  
        		ball_score = CalculateRuns(r, batsman_1, bowler, cumulative_prob)
        		print("%d.%d\t%s\t%s\t%d" % (overs,b,batsman_1,bowler,ball_score))
        		

    		score += ball_score

    		if(ball_score%2):
        		batsman_1, batsman_2 = batsman_2, batsman_1

    		# End of Over    
    		if(b == 6 and numberOfBalls<120):
        		batsman_1, batsman_2 = batsman_2, batsman_1
        		bowler_index += 1
        		bowler = bowlerOrder[bowler_index].rstrip("\n")
        		b = 0
        		overs +=1
	print("Final Score :",score)
	if(score == Target):
    		print("Tie")
	elif(Target > score):
    		print("Team 1 wins by %d runs"%(Target-score))
	elif(Target < score):
		print("Team 2 wins by %d wickets"%(10-wickets))

print("First Innings")
Target = Innings1()
print("Second Innings")
Innings2(Target)