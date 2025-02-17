import sqlite3

## connect to sqllite
connection=sqlite3.connect("student.db")

##create a cursor object to insert record,create table
cursor=connection.cursor()

## create the table
table_info="""
create table STUDENT(NAME VARCHAR(25),CLASS VARCHAR(25),
SECTION VARCHAR(25),MARKS INT)
"""

cursor.execute(table_info)

## Insert some more records
cursor.execute('''Insert Into STUDENT values('Krish','Data Science','A',90)''')
cursor.execute('''Insert Into STUDENT values('John','Data Science','B',100)''')
cursor.execute('''Insert Into STUDENT values('Mukesh','Data Science','A',86)''')
cursor.execute('''Insert Into STUDENT values('Jacob','DEVOPS','A',50)''')
cursor.execute('''Insert Into STUDENT values('Dipesh','DEVOPS','A',35)''')
cursor.execute("Insert Into STUDENT values('Aditi','Mathematics','B',85)")
cursor.execute("Insert Into STUDENT values('Suresh','Physics','A',78)")
cursor.execute("Insert Into STUDENT values('Meera','Chemistry','C',92)")
cursor.execute("Insert Into STUDENT values('Rohan','Biology','B',88)")
cursor.execute("Insert Into STUDENT values('Priya','History','A',74)")
cursor.execute("Insert Into STUDENT values('Ankit','Mathematics','C',81)")
cursor.execute("Insert Into STUDENT values('Rita','Geography','B',89)")
cursor.execute("Insert Into STUDENT values('Vikas','Physics','A',77)")
cursor.execute("Insert Into STUDENT values('Lakshmi','Data Science','B',95)")
cursor.execute("Insert Into STUDENT values('Jay','Mathematics','C',66)")
cursor.execute("Insert Into STUDENT values('Sonal','English','A',87)")
cursor.execute("Insert Into STUDENT values('Ravi','Mathematics','B',72)")
cursor.execute("Insert Into STUDENT values('Sneha','Chemistry','A',90)")
cursor.execute("Insert Into STUDENT values('Tarun','Biology','C',83)")
cursor.execute("Insert Into STUDENT values('Arjun','Physics','B',79)")
cursor.execute("Insert Into STUDENT values('Kavita','History','A',91)")
cursor.execute("Insert Into STUDENT values('Aakash','Geography','C',88)")
cursor.execute("Insert Into STUDENT values('Nisha','English','B',85)")
cursor.execute("Insert Into STUDENT values('Manoj','Chemistry','A',93)")
cursor.execute("Insert Into STUDENT values('Divya','Biology','C',76)")
cursor.execute("Insert Into STUDENT values('Ganesh','Mathematics','B',82)")
cursor.execute("Insert Into STUDENT values('Pooja','Physics','A',89)")
cursor.execute("Insert Into STUDENT values('Sahil','History','C',80)")
cursor.execute("Insert Into STUDENT values('Anita','Data Science','B',94)")
cursor.execute("Insert Into STUDENT values('Kiran','English','A',78)")


## Display all the records
print("The inserted records are")
data=cursor.execute('''Select * from STUDENT''')
for row in data:
    print(row)

## Commit your changes in the database
connection.commit()
connection.close()
