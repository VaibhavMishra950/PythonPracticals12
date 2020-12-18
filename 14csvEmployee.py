import csv

def add():
	id = int(input("Enter Employee Id: "))
	f.seek(0)
	reader = csv.reader(f)
	writer = csv.writer(f)
	for x in reader:
		if int(x[0]) == id:
			print("Employee Already exists")
			break
	else:
		name = input("Enter Employee Name: ")
		dept = input("Enter Employee Department: ")
		sal = float(input("Enter Employee Salary: "))
		data = [id, name, dept, sal]
		writer.writerow(data)
		print("Data Added Succeasfully.")

def search():
	id = int(input("Enter Employee Id: "))
	f.seek(0)
	reader = csv.reader(f)
	for x in reader:
		if int(x[0]) == id:
			print("Data Found!!")
			print("Employee ID: ", x[0])
			print("Employee Name: ", x[1])
			print("Employee Department: ", x[2])
			print("Employee Salary: ", x[3])
			break
	else:
		print("Data Not Found!!")

def display():
	print("Emp ID    Emp Name")
	f.seek(0)
	reader = csv.reader(f)
	for x in reader:
		print(x[0], "\t", x[1])


f = open("Files/employee.csv", "a+")

menu = """

1.  Add Employee
2.  Search Employee
3.  Display Employees
4.  Exit

"""
while True:
	print(menu)
	ch = int(input("Enter Your Choice [1-4]: "))
	
	if ch == 1:
		add()
	
	elif ch == 2:
		search()
	
	elif ch == 3:
		display()
	
	elif ch == 4:
		exit()
	
	else:
		print('Invalid Choice!!')
	
	print("\n#########################################\n")
	