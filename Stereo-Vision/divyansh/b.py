import numpy as np

import scipy

import matplotlib.pyplot as plt

import math

import csv

import cv2 as cv

from PIL import Image

# fields = [] 
# rows = [] 
  
# # reading csv file 
# with open(filename, 'r') as csvfile: 
#     # creating a csv reader object 
#     csvreader = csv.reader(csvfile) 
      
     
    
  
#     # extracting each data row one by one 
#     for row in csvreader: 
#         rows.append(row)

imgR = cv.imread('edge2.png',0)
imgL = cv.imread('edge3.png',0)

BOOL_LEFT = True
SIZE_ = 7
RANGE_ = 90
THRESH_ = 1

###############################
####   Mapping function    ####

def right_map(i,j):
    global l_im
    global r_im
    global RANGE_
    global THRESH_
    global SIZE_
    global imgR

    min_cost = 10000
    min_k = 10000

    for k in range(RANGE_):
        cost = 0
        den1 = 0
        den2 = 0
        for it1 in range(SIZE_):
            for it2 in range(SIZE_):
                if((j+it2-k>=0) and (j-k>=0) and (int(imgR[i,j-k])==255)) :
                	f = get_cost(i+it1,j+it2,j+it2-k)
                	cost = cost + f[0]
                	den1 = den1 + f[1]
                	den2 = den2 + f[2]
                else:
                	cost = 10000
        if cost !=10000:
        	cost = cost/math.sqrt(den1*den2)
        	#print(cost)
        if cost<=min_cost:
            min_k = k
            min_cost = cost

    if(min_cost<THRESH_):
        return min_k
    else:
        return 10000

###############################
######   Square Error   #######

def get_cost(i,j_l,j_r):
    global l_im
    global r_im
    
    z = int(0)
    den1 = 0
    den2 = 0
    for k in range(3):

        z = z + (int(l_im[i,j_l][k])-int(r_im[i,j_r][k]))**2 
        den1 = den1 + int(l_im[i,j_l][k])**2
        den2 = den2 + int(r_im[i,j_r][k])**2

    return z,den1,den2

###############################

imL = cv.imread('left.png', 1)
imR = cv.imread('right.png', 1)

bord = int((SIZE_-1)/2)

l_im = cv.copyMakeBorder(imL, bord,bord,bord,bord, cv.BORDER_CONSTANT,value=[0,0,0])
r_im = cv.copyMakeBorder(imR, bord,bord,bord,bord, cv.BORDER_CONSTANT,value=[0,0,0])

height_left, width_left, channels_left = imL.shape
print(width_left)
print(height_left)
print(channels_left)

height_right, width_right, channels_right = imL.shape
print(width_right)
print(height_right)
print(channels_right)

assert width_left==width_right
assert height_left==height_right
assert channels_left==channels_right
assert channels_left==3

ht = height_left
wd = width_left

corr = np.ones((ht,wd))*wd*2
z = np.ones((ht,wd))*wd*2



print("Setting up correspondence")

for i in range(ht):

    print("At i="+str(i))
    
    for j in range(wd):
        if imgL[i,j] == 255:
            corr[i,j] = right_map(i,j)
        else:
            corr[i,j] = 0
        if(corr[i,j]==0):
            z[i,j] = 255
        elif(corr[i,j]>wd):
            z[i,j] = 255
        else:
            z[i,j] = 100*30/corr[i,j]



with open('disp_d_b.csv','w') as f:
    ppp = csv.writer(f)
    for g in range(ht):
        ppp.writerow(corr[g,:])
f.close()

with open('depth_d_b.csv','w') as f:
    ppp = csv.writer(f)
    for g in range(ht):
        ppp.writerow(z[g,:])
f.close()

imD = Image.new("L",(ht,wd))
pix = imD.load()
for i in range(ht):
    for j in range(wd):
        pix[i,j] = int(z[i,j])

imD.save('test_d_b.png','png')


imD = Image.new("L",(wd,ht))
pix = imD.load()
for i in range(ht):
    for j in range(wd):
        pix[j,i] = int(z[i,j])

imD.save('testk1_d_b.png','png')