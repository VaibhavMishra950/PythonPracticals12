digit = lower = upper = 0
f = open("Files/poem.txt", "r")
raw = f.read()
print("Contents of file: \n", raw)
print("\n")
for x in raw:
	if x.isdigit():
		digit+=1
	elif x.isupper():
		upper+=1
	elif x.islower():
		lower+=1
	else:
		pass
print("Digits: ", digit)
print("Lowercase: ", lower)
print("Uppercase: ", upper)
print("Alphabets: ", upper+lower)
