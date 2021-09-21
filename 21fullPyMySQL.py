#Python + MySQL

import mysql.connector as sql

con = sql.connect(
    host = "localhost",
    user = "",
    passwd = "",
    database = "test")

cursor = con.cursor()

def add_emp():
    cursor.execute('select * from employee')
    id = int(input("Enter Employee ID: "))
    for x in cursor.fetchall():
        if x[0] == id:
            print("Employee Already Exists!")
    else:
        name = input("Enter Employee Name: ")
        sal = int(input("Enter Employee Salary: "))
        age = int(input("Enter Employee Age: "))
        q = "insert into employee values({}, '{}', {}, {})"
        cursor.execute(q.format(id, name, sal, age))
        con.commit()
        print("Data Inserted.")

def show_emp():
    cursor.execute('select * from employee')
    for x in cursor.fetchall():
        print(x)


def update_emp():
    id = int(input("Enter Employee ID: "))
    cursor.execute('select * from employee')
    for x in cursor.fetchall():
        if x[0] == id:
            name = input("Enter New Name: ")
            sal = int(input("Enter New Salary: "))
            age = int(input("Enter New Age: "))
            st = "update employee set empname = '{}', empsal = {}, empage = {} where empid = {}"
            cursor.execute(st.format(name, sal, age, id))
            con.commit()
            print("Data Updated.")
            break
    else:
        print("Employee Not Found")


def del_emp():
    id = int(input("Enter Employee ID to Delete: "))
    cursor.execute('select * from employee')
    for x in cursor.fetchall():
        if x[0] == id:
            ask = input("Delete This Data (Y/N): ")
            if ask.lower() == 'y':
                cursor.execute('delete from employee where empid = {}'.format(id))
                con.commit()
                print("Data Deleted")
                break
            else:
                exit()

    else:
        print("Employee Not Found")

menu = """
1.  Add Employee
2.  Show Employee
3.  Update A Record
4.  Delete A Record
5.  Exit
"""

while True:
    print(menu)
    ch = int(input("Enter Your Choice [1-5]: "))
    if ch == 1:
        add_emp()
    elif ch == 2:
        show_emp()
    elif ch == 3:
        update_emp()
    elif ch == 4:
        del_emp()
    elif ch == 5:
        exit()
    else:
        print("Invalid Choice!!")
    print("****************************")


