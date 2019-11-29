from generateProbabilities import *

prob = generateProbabilities()
for i in prob.values():
    print(sum(list(i.values())))

