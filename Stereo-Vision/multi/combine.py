
import numpy as np
import scipy
import matplotlib.pyplot as plt
import math
import csv
import cv2 as cv


rows = []

with open('depth_1.csv', 'r') as csvfile: 
	# creating a csv reader object 
	csvreader = csv.reader(csvfile) 
	# extracting each data row one by one 
	for row in csvreader: 
		rows.append(row) 

csvfile.close()

z1 = np.array(rows)
z1 = z1.astype(np.float)

ht = len(z1)
wd = len(z1[0])

with open('depth_2.csv', 'r') as csvfile: 
	# creating a csv reader object 
	csvreader = csv.reader(csvfile) 
	# extracting each data row one by one 
	for row in csvreader: 
		rows.append(row) 

z2 = np.array(rows)
z2 = z2.astype(np.float)



csvfile.close()

for i in range(len(z1)):
    for j in range(len(z1[0])):
        if(z1[i,j]!=0 and z2[i,j]!=0):
            z1[i,j] = (z1[i,j]+z2[i,j])/2
        
        elif(z2[i,j]!=0):
            z1[i,j] = z2[i,j]

with open('depth_mix.csv','w') as f:
    p = csv.writer(f)
    for g in range(ht):
        p.writerow(z1[g,:])
f.close()