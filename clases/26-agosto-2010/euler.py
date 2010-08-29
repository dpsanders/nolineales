# Metodo de Euler, una sola variable

def f(x):
	return x

x0 = 1.
delta_t = 0.1

x = x0

t_final = 10.

t = 0.0

while t < t_final:
	x_nueva = x + delta_t * f(x)
	t += delta_t
	x = x_nueva
	print t, x
	
	
	
	
	
	



