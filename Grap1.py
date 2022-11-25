import matplotlib
import matplotlib.pyplot as plt
import numpy as np

#Definimos una lista
zonas = ['Las Rozas', 'Mostoles', 'Mordor', 'Aranjuez', 'Leganes']
#Definimos una lista con ventas como entero
ventas = [25, 32, 34, 20, 25]

fig, ax = plt.subplots()

ax.set_ylabel('Ventas')

ax.set_title('Cantidad de Ventas por Zona')
.
plt.bar(zonas, ventas)
plt.savefig('barras_simple.png')

plt.show()