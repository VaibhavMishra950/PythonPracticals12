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

id = int(input("Enter Emp ID to Delete Data: "))
d = "delete from employee where empid = {}".format(id)
cursor.execute(d)
con.commit()
print("Data Deleted")

print("\nNew Data")
cursor.execute(show)
for y in cursor.fetchall():
	print(y)


