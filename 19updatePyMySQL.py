import mysql.connector as sql
con = sql.connect(
		host = "localhost",
		user = "",
		passwd = "",
		database = "test")
cursor = con.cursor()
show = "select * from employee"
print("Old Data")
cursor.execute(show)
for x in cursor.fetchall():
	print(x)

id = int(input("Enter Emp ID to Update Data: "))
cursor.execute(show)
for x in cursor.fetchall():
	if x[0] == id:
		name = input("Enter New Name: ")
		sal = int(input("Enter New Salary: "))
		age = int(input("Enter New Age: "))
		update = "update employee set empname = '{}', empsal = {}, empage = {} where empid = {}"
		cursor.execute(update.format(name, sal, age, id))
		con.commit()
		break
else:
	print("Record Not Found")

print("\nNew Data")
cursor.execute(show)
for y in cursor.fetchall():
	print(y)


