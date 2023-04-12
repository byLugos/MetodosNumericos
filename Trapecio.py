import numpy as np
import matplotlib.pyplot as plt

def fx(x):
  y = np.sqrt(x)* np.sin(x)
  return y

a = 1
b = 3
n = 16
suma = 0
muestras = n+1
h = (b-a)/n
#PROCEDIMIENTO
for i in range(1, n):
  suma = suma + fx(a +      i * h)
total = h/2 * (fx(a) + 2*suma + fx(b))


#SALIDA
print('EL RESULTADO DE LA INTEGRAL CON ',n ,'TRAPECIOS ES ',total)

#PUNTOS
xi = np.linspace(a,b,muestras)
fi = fx(xi)

#LINEA
muestraLinea = muestras*10
xk = np.linspace(a,b,muestraLinea)
fk = fx(xk)

#TRAPECIOS
plt.plot(xi,fi,'go')
plt.plot(xk,fk)
plt.fill_between(xi,0,fi, color='b')
for j in range(muestras):
  plt.axvline(xi[j], color='w')
plt.show()