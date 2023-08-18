import sqlite3


connection = sqlite3.connect('user_for.db')


cursor = connection.cursor()

command = '''SELECT user_id FROM USERL;'''

cursor.execute(command)

result = cursor.fetchall()

print(result)