import sqlite3

# conn = sqlite3.connect("test.db")   # open or create
#
# print("Opened database successfully")

conn = sqlite3.connect("test.db")   # open or create

print("Opened database successfully")

c = conn.cursor()

sql = ""

c.execute(sql)
conn.commit()
conn.close()
print("Created successfully")