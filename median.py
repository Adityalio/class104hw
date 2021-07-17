import csv
import pandas as pd
with open("data.csv",newline='')as f:
    reader=csv.reader(f)
    data=list(reader)

data.pop(0)
weight=[]
for i in range(len(data)):
    ht=data[i][2]
    weight.append(float(ht))

total=0
n=len(weight)
weight.sort()
if n % 2==0:
    median1=float(weight[n//2])
    median2=float(weight[n//2-1])
    median=(median1+median2)/2
    
else:
    median=float(weight[n//2])

print(median)