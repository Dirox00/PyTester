curr = [ input().split() for _ in range(int(input())) ]
currencies = { i[1]:float(i[0]) for i in curr }
currencies['EUR'] = 1

x = input().split()
while x != ['.']:
	conversion = (float(x[0]) / currencies[x[1]]) * currencies[x[-1]] 
	print('%.2f %s = %.2f %s' % (float(x[0]), x[1], conversion, x[-1]))
	x = input().split()