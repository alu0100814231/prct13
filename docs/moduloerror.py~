#!/usr/bin/python
#!encoding: UTF-8

import moduloP8
import sys

def error(interv, n_test,umbral):
   suma=0
   for i in range(0,n_test):
     aprox = moduloP8.aprox(interv)

     if(abs(aprox - moduloP8.decimalespi)< umbral):
      suma = suma + 1
     porcentaje = (moduloP8.decimalespi/int(n))*100
     return porcentaje
  
              #Invocación de la función
if __name__=="__main__":           
  n = int(sys.argv[1]) 
  m = int(sys.argv[2])  #Declaramos n y m con este comando para que ejecutemos en el terminal directamente con, por ejemplo, python  aproxpi.py 10 10.
  u = float(sys.argv[3]) 
  print error(n,m,u)

   
   