y = float ( raw_input("Dame y: ") )

#x0 = y / 2.
x0 = 100000

x = x0		# x es la x actual, es decir x_n

n = 0

tolerancia = 1e-15

while abs(x*x - y) > tolerancia:
	x_nueva = 0.5*(x + (y/x) )
	
	x = x_nueva
	print x, x*x, x*x - y
	
	n += 1