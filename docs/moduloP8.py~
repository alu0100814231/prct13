#!/usr/bin/python
#!encoding: UTF-8

import sys                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
              #Declaración de la función
decimalespi = 3.1415926535897931159979634685441852
def aprox(n):  
  n=int(n)
  if(n>0):
    suma=0.0 
    for i in range(1,n+1):
      xi = ((i - 0.5)/float(n)) #funciones para hallar pi los float delante son para que lo que se sigue sera un float
      f_xi = 4/(1+xi**2)
      suma = suma + f_xi
      a = float(i-1)/n
      b = float(i)/n
      #print 'Subintervalo: [%f, %f] xi: %f f_xi: %f ' % (a, b, xi, f_xi)
 
  pi = suma/n
  return pi
              #Invocación de la función
if __name__=="__main__":           
  n = int(sys.argv[1]) 
  m = int(sys.argv[2])  #Declaramos n y m con este comando para que ejecutemos en el terminal directamente con, por ejemplo, python aproxpi.py 10 10.
  lista=[]
  for j in range(1,m+1): 
    aproxpi=aprox(j*m)  #declaramos esta función con j*m de veces
    lista.append(aproxpi) 
  print lista   