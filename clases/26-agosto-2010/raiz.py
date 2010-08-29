def raiz_cuadrada(y):
	# y es un argumento 
	x0 = 1
	
	x = x0		# x es la x actual, es decir x_n
	n = 0
	
	tolerancia = 1e-14	
	while abs(x*x - y) > tolerancia:
		x_nueva = 0.5*(x + (y/x) )
		
		x = x_nueva
		print x, x*x, x*x - y
		
		n += 1
		
	return x
