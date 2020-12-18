def getPrime(n):
	prime = []
	for num in range(2, n+1):
		temp = 0
		for x in range(2, num-1):
			if num % x == 0:
				temp = 1
				break
		if temp == 0:
			prime.append(num)
	return prime
	

ch = 'y'	
while ch.lower() == 'y':
	num = int(input("Enter the range: "))
	print("List of prime numbers: ", getPrime(num))
	ch = input("\nRun Again [ Y / N ] : ")
	
	