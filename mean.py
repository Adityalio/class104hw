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
for x in weight:
    total=total+x

mean=total/n
print(mean)
    
    