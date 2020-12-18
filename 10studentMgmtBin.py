import pickle
data = []
f = open("Files/studata_bin.dat", "wb+")
ch = 'Y'
while ch.lower()=='y':
	roll = int(input("Enter Roll No: "))
	name = input("Enter Name: ")
	marks = float(input("Enter Marks: "))
	temp = [roll, name, marks]
	data.append(temp)
	ch = input("Add More Data [Y/N]: ")

pickle.dump(data, f)
f.seek(0)
raw = pickle.load(f)
for x in range(len(raw)):
	print("Student", x+1)
	print("Roll No: ", raw[x][0])
	print("Name: ", raw[x][1])
	print("Marks: ", raw[x][2])
	print()

