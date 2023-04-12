import matplotlib.pyplot as plt
import numpy as np
from tabulate import tabulate
print("==============================\nMÉTODO DE BISECCIÓN\n==============================\n")

#FuncionOriginal
def function(x):
    y = x**(3)-2*x+5
    return y
#PROCEDIMIENTO
xi = -1
xu = -3
raiz = []
tabla=[]
err = 100.0
i = 1
iteracion=0
raiz.append(0)
while err > 0.0001:
    xr = (xi + xu) / 2.0
    if function(xi) * function(xr) > 0:
        xi = xr
        raiz.append(xr)
    else:
        xu = xr
        raiz.append(xr)
    err = float(abs((raiz[i] - raiz[i - 1]) / raiz[i]) * 100)
    i = i + 1
    iteracion=iteracion+1
    tabla.append([iteracion,xr])

#SALIDA
print(tabulate(tabla , headers=['Iteración','Xi']))
print("========================================\nLa raíz exacta es: ", xr,"\n========================================\n")
# GRAFICA
a = -10  
b = 5  
n = 50
xn = np.linspace(a, b, n)  
yn = function(xn)
plt.plot(xn, yn)
plt.grid(True)
plt.axhline(0, color="#ff0000") 
plt.axvline(0, color="#ff0000")  
plt.title("Metodo Biseccion")
plt.ylabel("Eje Y")
plt.xlabel("Eje X")
plt.plot(xr,0, 'ro')

if (xr!= np.nan):
    plt.axvline(xr)#Línea vertical donde cruzan la función idéntica y el g(x)
plt.show()