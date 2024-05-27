from server import mySql

cursor = mySql.connetion.cursor()
cursor.execute("SELECT * FROM test")
result = cursor.fetchall()
print(result)