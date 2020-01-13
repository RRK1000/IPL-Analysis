# **IPL-Analysis**

## **Problem statement**
To use previous IPL match data to simulate a match given:
* Teams
* Batting order
* Bowling order
* Toss decision
## **Implementation**
The idea is to generate probabilities of scoring 0, 1, 2, 3, 4, 5, or 6 runs or of a wicket for every batsman-bowler pair and simulate the score of the match ball-by-ball.

For handling unseen batsman-bowler pairs, we use two approaches:
### K-Means clustering
Implemented using Hadoop MapReduce, we cluster together similar batsmen and bowlers using certain parameters and then generate probabilities for each cluster-cluster pair.

### Collaborative filtering
This method uses Spark's MLLib to perform Collaborative Filtering. It uses recommendation systems to generate values to fill empty batsman-bowler pair data.

## **Running the code**
* The first files to be generated are the data files using the codes in `/data/`
* All the code is available in `/src/` . The way to execute is, execute `./run.sh` from both, the batsmen and bowler directories. This runs the k-means code using MapReduce.
* Match simulation code is in `/src/probcalc/`.
* First change `Team1bats.csv`, `Team1bowl.csv`, `Team2bats.csv`, `Team2bowl.csv` to Team 1 batting order, Team 1 bowling order, Team 2 batting order and Team 2 bowling order respectively in both, `/CollaborativeFiltering/` and `/KMeansClustering/`.
* Run `run.sh` in `/CollaborativeFiltering/` and `simMatch.py` in `/KMeansClustering/` to simulate matches using both strategies.
* This will give you the ball-by-ball simulated output for every match.
