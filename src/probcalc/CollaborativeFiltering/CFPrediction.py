#
# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

"""
Collaborative Filtering Classification Example.
"""
from __future__ import print_function

from pyspark import SparkContext
import sys

# $example on$
from pyspark.mllib.recommendation import ALS, MatrixFactorizationModel, Rating
# $example off$

if __name__ == "__main__":
    fp = open("./data/p"+str(sys.argv[1])+"_pred.csv", "w")
    sc = SparkContext(appName="PythonCollaborativeFilteringExample")
    # $example on$
    # Load and parse the data
    data = sc.textFile("./data/p"+str(sys.argv[1])+".csv")
    batsmen = {}
    b1 = {}
    batsmen_index = 0
    bowlers = {}
    b2 = {}
    bowlers_index =0
    for line in data.collect():
        line = line.split(',')
        if(line[0] not in b1.keys()):
            batsmen[batsmen_index] = line[0]
            b1[line[0]] = batsmen_index
            batsmen_index+=1

        if(line[1] not in b2.keys()):
            bowlers[bowlers_index] = line[1]
            b2[line[1]] = bowlers_index
            bowlers_index+=1

    ratings = data.map(lambda l: l.split(','))\
        .map(lambda l: Rating(b1[l[0]], b2[l[1]], float(l[2])))

    # Build the recommendation model using Alternating Least Squares
    rank = 10
    numIterations = 10
    model = ALS.train(ratings, rank, numIterations)

    # Evaluate the model on training data
    testdata = ratings.map(lambda p: (p[0], p[1]))
    predictions = model.predictAll(testdata).map(lambda r: ((r[0], r[1]), r[2]))
    ratesAndPreds = ratings.map(lambda r: ((r[0], r[1]), r[2])).join(predictions)
    for item in predictions.collect():
        fp.write(batsmen[item[0][0]]+','+bowlers[item[0][1]]+',' + str(item[1])+'\n')

    MSE = ratesAndPreds.map(lambda r: (r[1][0] - r[1][1])**2).mean()
    print("Mean Squared Error = " + str(MSE))

    # Save and load model
    model.save(sc, "models/target"+str(sys.argv[1])+"/tmp/myCollaborativeFilter")
    sameModel = MatrixFactorizationModel.load(sc, "models/target"+str(sys.argv[1])+"/tmp/myCollaborativeFilter")
    fp.close()
    # $example off$
