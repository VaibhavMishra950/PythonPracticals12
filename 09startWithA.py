f1 = open("Files/report.txt", "r")
f2 = open("Files/final.txt", "w+")
data = f1.readlines()
print("Contents of Report File: \n")
for x in data:
	print(x, end = "")
	if x[0].lower() == 'a':
		f2.write(x)
print("\n")
print("Contents of Final File: \n")
f2.seek(0)
for x in f2.readlines():
	print(x, end = "")