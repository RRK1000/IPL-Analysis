fp = open("alldata.csv", "r")

fp1 = open("alldata2017.csv","w")

flag = 0
for line in fp.readlines():
    line = line.split(',')
    if(len(line)>2):
        if (line[1]=="season") and ("2017" in line[2]):
            flag = 1
        elif (line[1]=="season") and ("2017" not in line[2]):
            flag = 0
        
        if flag and (line[0] == "ball"):
            fp1.write((",".join(line)).rstrip("\",\"\n")+'\n')
 
