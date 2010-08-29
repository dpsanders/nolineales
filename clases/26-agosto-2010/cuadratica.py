#y = float ( raw_input("Dame a, b, c: ") )

from raiz import *

from math import *
	

a = 1
b = 0
c = 10


discriminante  = b*b - 4*a*c

if discriminante < 0.0:
	#print " NO PUEDO! " 
	raices_complejos = True
	discriminante = -discriminante
else:
	raices_complejos = False


	#x0 = y / 2.

x = raiz_cuadrada(discriminante)

print "HOLA"	

print "x =", x
print "sqrt = ", sqrt(discriminante)
print x - sqrt(discriminante)

if raices_complejos:
	x = x * 1j

print "Primera raiz: ", (-b + x) / (2.*a)
print "Segunda raiz: ", (-b - x) / (2.*a)

	
	
	









