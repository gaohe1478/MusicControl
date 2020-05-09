import csv
import random
with open("dnntest.csv",'w',newline='') as t:
    writer = csv.writer(t)
    #writer.writerow(["delta", "theta", "lowalpha", "highalpha", "lowbeta", "highbeta" , "lowgamma", "highgamma", "att"])
    i=0
    while i<100:
        #writer.writerow(["delta", "theta", "lowalpha", "highalpha", "lowbeta", "highbeta"  "lowgamma", "highgamma", "att"])
        writer.writerow([random.randint(0,9),random.randint(0,9),random.randint(0,9),random.randint(0,9),random.randint(0,9),random.randint(0,9),random.randint(0,9),random.randint(0,9),0])
        writer.writerow([random.randint(10,20),random.randint(10,20),random.randint(10,20),random.randint(10,20),random.randint(10,20),random.randint(10,20),random.randint(10,20),random.randint(10,20),1])
        i=i+1
        writer.writerow([random.randint(21,30),random.randint(21,30),random.randint(21,30),random.randint(21,30),random.randint(21,30),random.randint(21,30),random.randint(21,30),random.randint(21,30),2])