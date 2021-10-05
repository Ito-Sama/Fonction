import os
from matplotlib.pylab import plot
import matplotlib.pyplot as plt
import  numpy  as  np 
from math import *

print("petit programme pour trouver l'image et l'antecedent d'une simple fonction f(x)")
print("pour modifier la fonction, modifier la variable 'fonc'")
print("premiere colone = image et deuxieme colone = antecedent")
print()
f = input(">")
print("fonction", f, ":")
print()

y = []


def fonction(x):
    e = eval(f)
    y.append(e)
    return e 
    
    
for x in range(1,20):
    x = x + 1
    print(x, ":", fonction(x))


X = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15, 16, 17, 18, 19, 20]
Y = y

print(plot(X, Y))

fig = plt.figure() 
ax = plt.axes(projection = '3d')

# Data for a three-dimensional line
zline = np.linspace(0, 15, 19)
xline = X
yline = Y

print(ax.plot3D(xline, yline, zline, 'blue'))
   
    
    

os.system("pause")

