import mysql.connector

# Establish connection
cnx = mysql.connector.connect(
    auth_plugin='mysql_native_password',
    host='localhost',
    user='root',
    password='aryan2703',
    database='traindata_db'
    
)

# Create cursor
cursor = cnx.cursor()

# Execute query
query = "SELECT * FROM table_name"
cursor.execute(query)

# Fetch and display the result
result = cursor.fetchall()
for row in result:
    print(row)

# Close cursor and connection
cursor.close()
cnx.close()
