import matplotlib.pyplot as plt
import numpy as np
t = np.linspace(0,2*np.pi,400)
x = np.cos(t)
y = np.sin(t)
puntos = 1000000
print(1)
coordenadas_en_x = 2*np.random.rand(puntos,1)-1
print(2)
coordenadas_en_y = 2*np.random.rand(puntos,1)-1
print(3)
plt.plot(x, y,'r')
print(4)
colores = []
cont_adentro = 0
for i in range(puntos):
    if coordenadas_en_x[i]**2+coordenadas_en_y[i]**2>1:
        colores.append('#0000FF')
    else:
        colores.append('#00FF00')
        cont_adentro+=1
print(5)
print("pi es aproximadamente igual a ", cont_adentro*4/puntos)
plt.scatter(coordenadas_en_x,coordenadas_en_y,c=colores)
print(6)
plt.gca().set_aspect('equal', adjustable='box')
plt.show()