#!/usr/bin/python

#!ecoding: UTF-8

import matplotlib.pyplot as plt 
import math
import time
import moduloP8
import moduloerror
#Declaramos las variables
Y=[]
n= [10,50,100,150,500,550,1000]
aprox = 100
for i in range (7):
    start=time.time()
    moduloerror.error(n[i], aprox, 1e-6)
    finish=time.time() - start
    Y = Y + [finish]
#nombre modulo.Comando que dibuja(parametros,estilo de la linea, color)

#el color suele determinarse por la primeraletra en ingles= red, magenta,blue, green, yellow, cyan, black(k),white.

#el linestyle puede ser ':','--','-.','-'

#el marker es la forma de los puntos de x,y =circle(o), square(s), pentagon(p), star(*), plus(+), dot(.),hexagon(h), dmont(d),(#)

b1=plt.subplot(211)

plt.title('Porcentajes de error')

# 1= filas, 2=columnas, 3= cuadrado en el que voy a poner los plot siguientes

plt.plot(n,Y,marker='s', linestyle='--', color='r', label='Linea 1')


#dibujo.xlabel('Texto eje X')

#dibujo.ylabel('Texto eje Y')

plt.legend()

plt.xlim(0.0,12.0)
plt.ylim(0.0,50.0)

#ticks es para que nos corte la grafica en un punto del eje
plt.xticks(x)
#dibujo.yticks()

b2= plt.subplot(212)

print "Introduzca 5 umbrales de error:"
umbral =[]
for i in range(5):
  print "Introduzca el umbral", i, ":"
  umbral.append(float(raw_input()));
print"Introduzca el nombre fichero resultados"
if (n>o):
  try:
    fichero = open (nombre_fichero, "a")
  except:
    fichero = open (nombre_fichero, "w")
  fichero.write("num de intervalos: %d\n"%(aproximaciones))
  for i in range (5):
    start=time.time()
    moduloerror(n, aproximaciones, umbral[i])
    finish=time.time() - start
    t1=timeit.Timer("modulo.error(n.aproximaciones,umbral)","from__main__import modulo; n=%d; aproximaciones=%d;umbral=%f"(n,aproximaciones, umbral[i]))
    print t1.timeit(10)
    fichero.write("%2.10f\n"%(finish))
    fichero.close()
else:
  print "El valor de los intervalos debe ser mayor que 0"
    

plt.plot(x1, y1, marker='h', linestyle='-',
color='m', label= 'Linea4')

plt.plot(x2, y2, marker='*', linestyle=':',
color='b', label= 'Linea5')


#dibujo.title('Titulo del dibujo')

plt.xlabel('Intervalos')
plt.ylabel('Tiempo en segundos')

#dibujo.legend()


#indicamos el limite de los ejes, para que la funcion quede mas centrada y se vea mejor

plt.xlim(3.0,12.0)
plt.ylim(0.0,60.0)

plt.show()