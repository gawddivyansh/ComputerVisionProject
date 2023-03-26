
import numpy as np
import matplotlib.pyplot as plt
import csv
import cv2 as cv
from PIL import Image


###############################
#####  PARAMETER VALUES  ######

BOOL_LEFT = True
SIZE_ = 7
RANGE_ = 90
THRESH_ = 750

###############################
####   Mapping function    ####

def right_map(i,j):
    global l_im
    global r_im
    global RANGE_
    global THRESH_
    global SIZE_

    min_cost = 10000
    min_k = 10000

    for k in range(RANGE_):
        cost = 0
        for it1 in range(SIZE_):
            for it2 in range(SIZE_):
                if(j+it2-k>=0):
                    cost = cost + get_cost(i+it1,j+it2,j+it2-k)
                else:
                    cost = 10000
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
    for k in range(3):
        '''
        print(i)
        print(j_l)
        print(j_r)
        print("___")
        '''
        z = z + (int(l_im[i,j_l][k])-int(r_im[i,j_r][k]))**2 

    return z

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
        corr[i,j] = right_map(i,j)
        if(corr[i,j]==0):
            z[i,j] = 255
        elif(corr[i,j]>wd):
            z[i,j] = 255
        else:
            z[i,j] = 150*50/corr[i,j]



with open('disp.csv','w') as f:
    ppp = csv.writer(f)
    for g in range(ht):
        ppp.writerow(corr[g,:])
f.close()

with open('depth.csv','w') as f:
    ppp = csv.writer(f)
    for g in range(ht):
        ppp.writerow(z[g,:])
f.close()

imD = Image.new("L",(ht,wd))
pix = imD.load()
for i in range(ht):
    for j in range(wd):
        pix[i,j] = int(z[i,j])

imD.save('test.png','png')


imD = Image.new("L",(wd,ht))
pix = imD.load()
for i in range(ht):
    for j in range(wd):
        pix[j,i] = int(z[i,j])

imD.save('testk1.png','png')