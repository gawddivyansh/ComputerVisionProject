import numpy as np
import csv
from PIL import Image

p=[]

with open('depth2.csv','r') as f:
    a = csv.reader(f)
    for x in a:
        p.append(x)

mint = int(290)
maxt = int(-1)

z = np.zeros((len(p),len(p[0])))
for i in range(len(p)):
    for j in range(len(p[0])):
        z[i,j] = float(p[i][j])
        #if(z[i,j]>255):
        #   z[i,j]=255

for i in range(len(p)):
    for j in range(len(p[0])):
        if(z[i][j] != 255):
            if(float(z[i][j])>maxt):
                maxt = z[i][j]
            if(float(z[i][j])<mint):
                mint = z[i][j]
print(maxt)
for i in range(len(p)):
    for j in range(len(p[0])):
        if(z[i,j] != 255):
            z[i,j] = 255*(z[i,j]-mint)/((maxt/27)-mint)        

imD = Image.new("L",(len(p[0]),len(p)))
pix = imD.load()
for i in range(len(p)):
    for j in range(len(p[0])):
        pix[j,i] = int(z[i,j])

imD.save('DEP3.png','png')
