import psycopg2

connection = psycopg2.connect(user="postgres",
                                password="123",
                                host="78.141.227.124",
                                port="5432",
                                database="postgres")
print('курсор')
cursor = connection.cursor()
print("PostgreSQL server information")

cursor.execute("SELECT * from students")
record = cursor.fetchall()
for i in record:
    print(i)
