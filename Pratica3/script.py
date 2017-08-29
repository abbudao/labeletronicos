import  csv
from statistics import mean
with open('exp222.csv','r') as csvfile:
    spam=csv.reader(csvfile,delimiter=',')
    a=[]
    b=[]
    for row in spam:
        a.append(eval(row[0]))
        b.append(eval(row[1]))
    print(min(b))
    print(max(b))
    print(mean(b))
