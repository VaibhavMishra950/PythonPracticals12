import pickle
f = open("Files/studata_bin.dat", "rb+")
data = pickle.load(f)
print("Old Data")
print(data)
ch = 'Y'
found = False
while ch.lower()=='y':
	roll = int(input("Enter Roll no to delete data: "))
	for x in data:
		if x[0]==roll:
			data.remove(x)
			print("Data Deleted")
			found = True
			break
	else:
		print("Data Not Found!")
	ch = input("Delete More [Y/N]: ")

if found:
	f.seek(0)
	pickle.dump(data, f)
f.seek(0)
print("Data After Deletion")
print(pickle.load(f))
