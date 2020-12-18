to = the = 0
f = open("Files/abc.txt", "r")
raw = f.read()
print(raw)
data = raw.split()

for x in data:
	if x=='to':
		to+=1
	elif x=='the':
		the+=1
	else:
		pass
print("\nNo. of \'to\' in file: ", to)
print("\nNo. of \'the\' in file: ", the)
