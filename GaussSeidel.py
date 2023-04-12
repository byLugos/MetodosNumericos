import matplotlib.pyplot as plt
import numpy as np

print("==============================\nMÉTODO DE GAUSS-SEIDEL\n==============================\n")
#INGRESO
A = [[1/2,0,-1/3,0] , [-7/2,5,0,-2/3], [-1/2,0,2,0], [0,-1/2,0,3/2]]
#Vector de terminos independientes
b = [1/4,1/2,1,3]
#INGRESO VALORES INICIALES
def gaussSeidel(tol,normaInicial,itMax,A,b):
  tolerancia = tol
  erp = normaInicial #Norma inicial
  kMax = itMax  #Maximo de iteraciones
  n = len(A) #Tamaño del vector
  x = np.zeros(n) #Vector inicial
  x1 = np.copy(x) #Vector auxiliar
  k = 1 #Iterador
  error1=[0] #Aux
  while k <= kMax and erp > tolerancia:
    print('Iteracion #',k)
    for i in range(n):
      sumatoria = 0
      for j in range(n):
        if i!=j:
          sumatoria += (A[i][j]*x[j])
      x[i] = (b[i]-sumatoria) / A[i][i]   
      print('Resultado en X(',i+1,') Es',x[i])
    erp = np.linalg.norm(x-x1) #Calcular la norma 
    error1.append(erp)
    x1 = np.copy(x)
    print('Norma',error1[k])
    print()
    k+=1

determinada = np.linalg.det(A) #Calcular el determinante
for h in range(len(A)):
  if A[h][h]==0:
    determinada=0
if determinada!= 0.0:
  print('El sistema si tiene solución')
  gaussSeidel(0.0001,100,25,A,b)
else:
  print('El sistema no tiene solución')