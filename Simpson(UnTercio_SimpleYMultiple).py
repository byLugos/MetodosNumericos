import numpy as np
import matplotlib.pyplot as plt
def fx(x):
  y = 2/(x**2-4)
  return y
def simpsonUno(a,b,f):
  h = (b-a) / 2
  total = h/3*(fx(a)+4*fx((a+h))+fx(b))
  print(total)
def simpsonDos(a,b,f,n):
    if n % 2 != 0 and n > 2:
        raise ValueError("HA INGRESADO UN 'N' QUE NO ES VÁLIDO")
    h = (b-a) / n
    suma = fx(a) + fx(b)
    for i in range(1, n, 2):
        suma += 4*f(a + i*h)
    for i in range(2, n-1, 2):
        suma += 2*f(a + i*h)
    total = h/3 * suma
    print (total)

def graficarSimpDos(a,b,n):
  muestras = n+1
  #PUNTOS
  xi = np.linspace(a,b,muestras)
  fi = fx(xi)
  #LINEA
  xk = np.linspace(a,b,(muestras*10))
  fk = fx(xk)

  plt.plot(xi,fi,'ro')
  plt.plot(xk,fk)
  plt.fill_between(xi,0,fi, color='b')
  for j in range(muestras):
    plt.axvline(xi[j], color='w')
  plt.show()

  
a = 0
b = 0.35
condicion = 1
print('DIGITE LA OPCIÓN DESEADA')
while condicion == 1:
    print('1. SIMPSON CUANDO ES = 2\n2. SIMPSON CUANDO ES <2 PERO EXCLUSIVAMENTE PAR')
    decision = input()
    try:
        Castdecision = int(decision)
        if Castdecision == 1:
            print('MÉTODO DE SIMPSON N = 2')
            print('EL RESULTADO DE LA FUNCIÓN ES')
            simpsonUno(a,b,fx)
            condicion = 2
        elif Castdecision == 2:
            print('MÉTODO DE SIMPSON N > 2 Y PAR')
            print('EL RESULTADO DE LA FUNCIÓN ES')
            simpsonDos(a,b,fx,10)
            graficarSimpDos(a,b,100)
            condicion = 2
        else:
            print('DIGITE UN VALOR VÁLIDO EN LAS OPCIONES')
    except ValueError:
        print('DIGITE ÚNICAMENTE VALORES VÁLIDOS PARA EVALUAR')



