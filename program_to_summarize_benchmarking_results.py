import os

## first decide which are the information that you want
## what have i captured in the csv:
## 
## 

baseDir = "/home/sashank/Documents/Benchmarking/aws_BenchmarkingResults/awsMumbai-t2Micro/1users"
fileNm = "result_1288.csv"

filePath = baseDir+"/"+fileNm

fopen = open(filePath,"r")
fList = fopen.read().split("\n")
fopen.close()

fListLen = len(fList)

cummulTime = 0.0
prevcummulTime = 0.0
for iter in range(len(fList)):
   if iter in (0,1):
      pass ## why? this is because - we want to skip the header and the second line
   elif iter in ((fListLen-1),(fListLen-2)):
      pass ## because the last line is newline and second last line is total time elapsed
   else:
      #print str(fList[iter])
      lineList = str(fList[iter]).split(",")
      #print lineList[0]
      cummulTime = float(lineList[2]) + prevcummulTime
      print "cummulTime == "+str(cummulTime)+"\n"
      prevcummulTime = cummulTime
   




