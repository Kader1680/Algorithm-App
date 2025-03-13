from faker import Faker  
import pymysql

fake = Faker()

mydb = None
mycursor = None

try:
    mydb = pymysql.connect(
        host="localhost",
        user="root",
        password="",  
    )
    mycursor = mydb.cursor()

    mycursor.execute("CREATE DATABASE IF NOT EXISTS azeDB")   
    mycursor.execute("USE azeDB")   

    mycursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        id INT AUTO_INCREMENT PRIMARY KEY, 
                        name VARCHAR(255), 
                        email VARCHAR(255)
                    )''')

    users = [(fake.name(), fake.email()) for _ in range(100000)]

    mycursor.executemany("INSERT INTO users (name, email) VALUES (%s, %s)", users)
    
    mydb.commit()

    print("100,000 users inserted successfully!")

except pymysql.MySQLError as e:
    print("Error connecting to MySQL:", e)

finally:
    if mycursor is not None:
        mycursor.close()
    if mydb is not None:
        mydb.close()
