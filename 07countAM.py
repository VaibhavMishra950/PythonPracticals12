a = m = 0
f = open("Files/test.txt", "r")
data = f.readlines()
for x in data:
	if x[0]=='A' or x[0]=='a':
		a+=1
	elif x[0]=='M' or x[0]=='m':
		m+=1
	else:
		pass

print("No of A in file: ", a)
print("No of M in file: ", m)