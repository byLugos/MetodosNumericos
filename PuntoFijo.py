import matplotlib.pyplot as plt
import numpy as np
from tabulate import tabulate


print("==============================\nMÉTODO DE PUNTO FIJO\n==============================\n")
#Funcion Original
def funcionNormal(x):
    fdeX= (x**(3)-(2*x)+5)
    return fdeX
#Despejamos X
def despejadaX(x):
    gdeX = np.cbrt(2*x-5)
    return gdeX
#PROCEDIMIENTO
aux = []
iteracion=0
x = 1 #valor inicial
errorF = 0.00000001
err = 100
i = 1;
tabla=[]
aux.append(x)
while abs(err) > errorF:
    xs = despejadaX(x)
    aux.append(xs)
    err = ((aux[i]-aux[i-1])/aux[i])*100
    x = xs
    i +=1
    iteracion+=1
    tabla.append([iteracion,x])

#SALIDA
print(tabulate(tabla , headers=['Iteración','Xi']))
print("========================================\nLa raíz exacta es: ", x,"\n========================================\n")
#GRAFICA
a = -5   #CAMBIAR SEGUN LA FUNCION, DEBE ESTAR DENTRO DE UN INTERVALO PARA QUE SE VEA TODA LA FUNCION
b = 2  
n = 100  
xn = np.linspace(a, b, n) 
yn = funcionNormal(xn)
plt.plot(xn, yn) 
plt.grid(True)
plt.axhline(0, color="#ff0000")  
plt.axvline(0, color="#ff0000")  
plt.plot(x, 0, 'ko') 
plt.title("Metodo Punto fijo")
plt.ylabel("Eje Y")
plt.xlabel("Eje X")
if (x!= np.nan):
    plt.axvline(x)#Línea vertical donde cruzan la función idéntica y el g(x)
plt.show()