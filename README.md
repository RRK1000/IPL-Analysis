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
* All the code is available in `/src/` . The way to execute is, first run `createcentroids.py` and then execute `./run.sh` . This runs the k-means code using MapReduce.
* [IMPLEMENT COLLABORATIVE FILTERING]
* [IMPLEMENT PROBABILITY CALCULATION]
* [IMPLEMENT MATCH SIMULATION]
* [IMPLEMENT ACCURACY CALCULATION]