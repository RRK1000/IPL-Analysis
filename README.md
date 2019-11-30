# **IPL-Analysis**

## **Problem statement**
To use previous IPL match data to simulate a match given:
* Teams
* Batting order
* Bowling order
* Toss decision
## **Implementation**
The idea is to generate probabilities for every batsman-bowler pair and simulate the score of the match ball-by-ball.

For handling unseen batsman-bowler pairs, we use k-means clustering, implemented using Hadoop MapReduce, to cluster together similar batsmen and bowlers and then generate probabilities for these clusters.

We also use collaborative filtering to predict the probabilities for unseen batsman-bowler pairs and compare it with the k-means approach.

## **Running the code**
* The first files to be generated are the data files using the codes in `/data/`
* All the code is available in `/src/` . The way to execute is, execute `./run.sh` from both, the batsmen and bowler directories. This runs the k-means code using MapReduce.
* [PLS MAKE A CF ./run.sh FILE]
* [CHANGE FOLDER STRUCTURE SO THATCF IS A SEPARATE FOLDER AND PROBCALC IS A SEPARATE FOLDER]
* [FINISH MATCH SIMULATION]
* [IMPLEMENT ACCURACY CALCULATION]
