ch = 'Y'
f = open("Files/studata.txt", "w")
while ch.lower()=='y':
	roll = int(input("Enter Roll No: "))
	name = input("Enter Student Name: ")
	marks = float(input("Enter Marks: "))
	data = str(roll)+", "+name+", "+str(marks)+"\n"
	f.write(data)
	ch = input("\nEnter More Data [Y/N]: ")
f.close()
f=open("Files/studata.txt", "r")
raw = f.readlines()
count = len(raw)
for x in range(count):
	print("Data of student", x+1)
	print(raw[x])
	
	