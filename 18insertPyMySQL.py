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

id = int(input("\nEnter Emp ID: "))
name = input("Enter Emp Name: ")
sal = int(input("Enter Emp Salary: "))
age = input("Enter Emp Age: ")

insert = "insert into employee values({}, '{}', {}, {})".format(id, name, sal, age)
cursor.execute(insert)
con.commit()
print("\nNew Data")
cursor.execute(show)
for y in cursor.fetchall():
	print(y)


