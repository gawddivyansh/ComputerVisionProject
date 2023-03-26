import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D



# get 2D z data
Z = np.loadtxt("final_depth_NEW.csv", delimiter=",")

X,Y = np.meshgrid( np.arange(0,len(Z[0]),1),np.arange(0,len(Z),1))

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.plot_surface(X, Y, Z)

plt.show()