import mysql.connector

# Connect to MySQL Server
conn = mysql.connector.connect(
    host="localhost",
    user="Ixa",       # Replace with your MySQL username
    password="Man@1234"    # Replace with your MySQL password
)
cursor = conn.cursor()

# a. Create a database COMPUTER_DB
cursor.execute("CREATE DATABASE IF NOT EXISTS COMPUTER_DB")

# b. Set connection with COMPUTER_DB
cursor.execute("USE COMPUTER_DB")

# c. Create a table STUDENT_SELECTION
cursor.execute("""
    CREATE TABLE IF NOT EXISTS STUDENT_SELECTION (
        FIRST_NAME VARCHAR(50),
        LAST_NAME VARCHAR(50),
        AGE INT,
        GENDER CHAR(1),
        SCORE FLOAT
    )
""")

# d.i Add a column ADDRESS
cursor.execute("ALTER TABLE STUDENT_SELECTION ADD COLUMN ADDRESS VARCHAR(100)")

# d.ii Insert a record
insert_query = """
    INSERT INTO STUDENT_SELECTION (FIRST_NAME, LAST_NAME, AGE, GENDER, SCORE, ADDRESS)
    VALUES (%s, %s, %s, %s, %s, %s)
"""
student_data = ("John", "Doe", 20, "M", 85.5, "New York")
cursor.execute(insert_query, student_data)

# d.iii Update males' age by 1 year
cursor.execute("UPDATE STUDENT_SELECTION SET AGE = AGE + 1 WHERE GENDER = 'M'")

# d.iv Delete records where AGE is less than 18
cursor.execute("DELETE FROM STUDENT_SELECTION WHERE AGE < 18")

# Commit changes and close the connection
conn.commit()
cursor.close()
conn.close()
