import math
ch='y'
while(ch.lower() == 'y'):
	x=float(input('Enter the value of X in degrees: '))
	radian=math.radians(x)
	print('Value of X in Radians=',radian,'and in Degree=',x)
	terms=int(input('enter the number of terms: '))
	b=0 
	for i in range (terms):
		a=(((((-1)**i))*(radian**((2*i)+1)))/(math.factorial((2*i)+1))) 
		b+=a
	print('1. Radian value of sin(X) computed according to tayler series: ',b)
	print('2. Radian value of sin(X) correct value as math formula: ',math.sin(radian))
	print('Now compare the correct value in step 1 with step 2')
	ch=input('continue [ Y / N ]: ')