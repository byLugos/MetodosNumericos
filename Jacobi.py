import matplotlib.pyplot as plt
import numpy as np

print("==============================\nMÉTODO DE JACOBI\n==============================\n")
#INGRESO
A = [[2,1,0],[1,2,0],[1,1,1]]
b = [5,8,6] #independiente
#INGRESO VALORES INICIALES
def jacobiMetodo(tol,normaInicial,itMax,A,b):
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
          sumatoria += (A[i][j]*x1[j])
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
  jacobiMetodo(0.0001,100,25,A,b)
else:
  print('El sistema no tiene solución')
