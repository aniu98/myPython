import sqlite3
import datetime

con = sqlite3.connect('mydatabase.db')
cursorObj = con.cursor()
cursorObj.execute('create table if not exists projects(id integer, name text)')
data = [(1, "Ridesharing"), (2, "Water Purifying"), (3, "Forensics"), (4, "Botany")]
cursorObj.executemany("INSERT INTO projects VALUES(?, ?)", data)
con.commit()
# 处理日期

#TODO  The default date adapter is deprecated as of Python 3.12; see the sqlite3 documentation for suggested replacement recipes
#TODO   cursorObj.executemany("INSERT INTO assignments VALUES(?, ?, ?)", data)
cursorObj.execute('create table if not exists assignments(id integer, name text, date date)')
data = [(1, "Ridesharing", datetime.date(2017, 1, 2)), (2, "Water Purifying", datetime.date(2018, 3, 4))]
cursorObj.executemany("INSERT INTO assignments VALUES(?, ?, ?)", data)
con.commit()

con.close()