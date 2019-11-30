from CFprobabilities import *

def CP():
	cp = dict()
	prob = CFprobabilities()

	for i in prob:
		cp[i] = {0: 0.0, 1: 0.0, 2: 0.0, 3: 0.0,4: 0.0, 5: 0.0, 6: 0.0}


	for i in prob:
		for j in prob[i]:
			t = 0
			while(j!="W" and j!="B" and t<=int(j)):
				cp[i][j] = cp[i][j]+prob[i][t]
				t = t+1

	return cp
