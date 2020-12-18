import pickle
f = open("Files/studata_bin.dat", "rb")
raw = pickle.load(f)
ch='Y'
while ch.lower()=='y':
	roll = int(input("Enter Roll No To Search: "))
	for x in raw:
		if x[0] == roll:
			print("Record Found!\n")
			print("Roll No:", x[0])
			print("Name:", x[1])
			print("Marks:", x[2])
			print()
			break
	else:
		print("No Records Found!!")
	ch = input("Search Again [Y/N]: ")
