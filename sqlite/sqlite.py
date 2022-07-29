import sqlite3
 
con = sqlite3.connect('mydatabase.db')
cursorObj = con.cursor()

cursorObj.execute('SELECT * from sqlite_master where type= "table"')
cursorObj.execute('SELECT name from sqlite_master where type= "table"')
print("查询所有的表： "+str(cursorObj.fetchall()) )

cursorObj.execute("CREATE TABLE if not exists employees(id integer PRIMARY KEY, name text, salary real, department text, position text, hireDate text)")


print("ss")

def sql_insert(con, entities):
    cursorObj = con.cursor()
    # cursorObj.execute("INSERT INTO employees VALUES(1, 'John', 700, 'HR', 'Manager', '2017-01-04')")
    cursorObj.execute('INSERT INTO employees(id, name, salary, department, position, hireDate) VALUES(?, ?, ?, ?, ?, ?)', entities)
    con.commit()
entities = (7, 'Andrew', 800, 'IT', 'Tech', '2018-02-06')
sql_insert(con, entities)

def sql_fetch(con):
    cursorObj = con.cursor()
    cursorObj.execute('SELECT * FROM employees')
    rows = cursorObj.fetchall()
    print(len(rows))
    for row in rows:
        print(row)

sql_fetch(con)
print(cursorObj.execute('SELECT * FROM employees').rowcount)