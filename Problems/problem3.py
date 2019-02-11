def isPrime(n):
    if n==2 or n==3: return True
    if n%2==0 or n<2: return False
    for i in range(3,n,2):   # Solo números impares
        if n%i==0:
            return False    
    return True

num = int(input())

while num > 0:
	if isPrime(num):
		print('%s is prime' % num)
	else:
		print('%s is not prime' % num)
	num = int(input())