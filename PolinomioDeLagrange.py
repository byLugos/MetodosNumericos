import matplotlib.pyplot as plt
import numpy as np
from tabulate import tabulate
import sympy as sym

print("==============================\nMÉTODO POLINOMIO DE LAGRANGE\n==============================\n")
#INGRESO
#Función original
xi = np.array([-3,-1,1,3,7])
fi = np.array([5,-0.5,-6,-1,8])
polinomio = 0 #Variable que guardará el polinomio
n = len(xi)
x = sym.Symbol('x') #Contiene un símbolo que se le puede asignar a una variable
#PROCEDIMIENTO
for i in range(0,n,1):
  numerador=1
  denominador=1
  for j in range(0,n,1):
    if (i!=j):
      numerador = numerador*(x-xi[j])
      denominador = denominador*(xi[i]-xi[j])
    termino = (numerador / denominador)*fi[i]
  polinomio = polinomio + termino
polisimple = sym.simplify_logic(polinomio) #Simplificar la expresión
#Se puede usar con expand de igual manera

#SALIDA
print('---Polinomio Completo---')
print(polinomio)
print('----------------------------------------------')
print('---Polinomio Simplificado---')
print(polisimple)
print('----------------------------------------------')


#GRÁFICA
funcionTraducida = sym.lambdify(x,polinomio) #Traduce las funciones Sympy en Phyton
a = -10
b = 10
n = 51
xn = np.linspace(a, b, n)  
yn = funcionTraducida(xn)
plt.plot(xi, fi,'ro')
plt.plot(xn,yn)
plt.grid(True)
plt.axhline(0, color="#ff0000") 
plt.axvline(0, color="#ff0000")  
plt.title("Método Polinomio de Lagrange")
plt.ylabel("Eje Y")
plt.xlabel("Eje X")