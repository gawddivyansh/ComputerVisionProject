import cv2
import numpy as np
from matplotlib import pyplot as plt
import csv

img = cv2.imread('right.png',0)
edges = cv2.Canny(img,100,200)

plt.subplot(121),plt.imshow(img,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
plt.imsave("edge2.png", edges,cmap = 'gray')
plt.show()
img = cv2.imread('edge2.png', 0)
print(img)
with open('data.csv', 'w') as file:
	file_writer = csv.writer(file, delimiter=',', quoting=csv.QUOTE_MINIMAL)
	for i in range(len(img)):
		file_writer.writerow(img[i])