#! /usr/bin/python
import sys
PI=3.14159265358979323846264338327950288

def h(n):

  if(n != 0):
    suma = 0
    for i in range(1,n+1):
      a = float(i-1)/float (n)
      b = float(i)/float (n)
      xi = float(i-0.5)/float (n)
      fxi = 4.0/(1.0 + xi*xi)
      #print  a, b, xi, fxi
      suma += fxi
    pi=float (suma)/float (n)
    return pi
    #print 'El valor aproximado de pi es: ', pi
    #print 'El valor de pi con 35 cifras decimales es: %1.35g' % PI

if __name__ == "__main__":
  
  if (len(sys.argv) != 3):
    n= int(raw_input('Introduzca el valor n: ')) 
    m= int(raw_input('Introduzca el valor m: '))
    
  else:
    n = int(sys.argv[1])
    m = int(sys.argv[2])
    
  lista=[]
  for i in range (1, m+1):
     pi=h(i*n)
     lista.append(pi)
  #print "pi: %.35f" % (pi)
  #print "El valor de pi con 35 cifras decimales es:%.35f" % (PI)
  print lista