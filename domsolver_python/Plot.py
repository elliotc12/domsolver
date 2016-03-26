import numpy as np
import matplotlib.pyplot as plt

def plot(array, xmax, ymax):
    x = np.arange(0.1,xmax,0.2)
    y = np.arange(0.1,ymax,0.2)

    X,Y = np.meshgrid(x,y)
    Z = np.zeros((len(x), len(y)))

    for a in array:
        Z[a[0]/0.2-1, a[1]/0.2-1] = a[2]
        
    print Z

    CS = plt.contourf(Z)
    cbar = plt.colorbar(CS)
    cbar.ax.set_ylabel('Victory points')
    plt.xlabel("Market preference")
    plt.ylabel("Village preference")
    plt.title("Victory points vs market/village preference")
    plt.show()
