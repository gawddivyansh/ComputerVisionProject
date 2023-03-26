import numpy as np

import scipy

import matplotlib.pyplot as plt

import math

import csv

import cv2 as cv

from PIL import Image

SIZE = 19

imgR = cv.imread('edge2.png',0)
imgL = cv.imread('edge3.png',0)

rows = []

with open('depth_d_b.csv', 'r') as csvfile: 
	# creating a csv reader object 
	csvreader = csv.reader(csvfile) 
	# extracting each data row one by one 
	for row in csvreader: 
		rows.append(row) 

zi = np.array(rows)
zi = zi.astype(np.float)
#print(zi.shape)

'''
gamma = 1e1


print('legen')
z = np.zeros(imgL.shape)
z_temp = np.zeros(imgL.shape)


for fpit in range(1000):
    for i in range(imgL.shape[0]):
        for j in range(imgL.shape[1]):
            try:
                if(zi[i,j]<=255):
                    z_temp[i,j] = (z[i+1,j]+z[i,j+1]+z[i-1,j]+z[i,j-1])/(4+gamma*(imgL[i,j]==255)) - zi[i,j]*gamma*(imgL[i,j]==255)/(4+gamma*(imgL[i,j]==255))
            except Exception as e:
                pass
			
    z = z_temp
    print('wait for it....' + str(fpit))




print('dary')
'''
def wtd(i,j):
    global imgL

    global SIZE

    wk = []
    zk = []

    for it1 in range(-SIZE,SIZE+1,1):
        for it2 in range(1,SIZE+1,1):
            if(imgL[i+it1,j+it2]==255):

                wk.append(np.sqrt(it1**2+it2**2))
                zk.append(zi[i+it1,j+it2])

    ret = 0
    den = 0

    for k in range(len(wk)):
        ret = ret + wk[k]*zk[k]
        den = den + wk[k] 

    if(den>0):
        return ret/den
    else:
        return 0


for i in range(SIZE,imgL.shape[0]-SIZE,1):
    for j in range(SIZE,imgL.shape[1]-SIZE,1):
        if(imgL[i,j]!=255):
            zi[i,j] = wtd(i,j)


with open('final_depth_NEW.csv', 'w') as file:
	file_writer = csv.writer(file, delimiter=',', quoting=csv.QUOTE_MINIMAL)
	for i in range(len(zi)):
		file_writer.writerow(50*100*zi[i])



