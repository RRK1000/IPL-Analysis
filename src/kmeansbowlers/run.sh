#!/bin/bash
i=1

while :
do
	$HADOOP_HOME/bin/hadoop jar /home/hadoop/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.2.0.jar -file centroids.txt -file ./mapper.py -mapper ./mapper.py -file ./reducer.py -reducer ./reducer.py -input /tmp/bowlerdata.csv -output /tmp/output$i
	rm -f centroids1.txt
	hadoop fs -copyToLocal /tmp/output$i/part-00000 centroids1.txt
	seeiftrue=`python reader.py`
	if [ $seeiftrue = 1 ]
	then
		rm centroids.txt
		hadoop fs -copyToLocal /tmp/output$i/part-00000 centroids.txt
		python mapper.py < batsmandata.csv > ../bowlerKMeansOutput.txt
		hadoop fs -rm -r /tmp/output*
		break
	else
		rm centroids.txt
		hadoop fs -copyToLocal /tmp/output$i/part-00000 centroids.txt
	fi
	i=$((i+1))
done
