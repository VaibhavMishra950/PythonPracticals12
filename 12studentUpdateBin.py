import pickle
found = 0
ch = 'Y'
f = open("Files/studata_bin.dat", "rb+")
raw = pickle.load(f)
print("Old Data")
print(raw)
while ch.lower()=='y':
	roll = int(input("Enter Roll No to Update: "))
	for x in raw:
		if x[0]==roll:
			print("Record Found")
			x[1] = input("Enter New Name: ")
			x[2] = float(input("Enter New Marks: "))
			found = 1
			break
	else:
		print("Record Not Found")
	ch = input("Update another Record [Y/N]: ")

if found == 1:
	f.seek(0)
	pickle.dump(raw, f)
f.seek(0)
data = pickle.load(f)
print("Data After Updating")
print(data)

		