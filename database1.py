import sqlite3

#creating database
conn = sqlite3.connect("10000coders.db")
cursor =conn.cursor()

#creating table
cursor.execute("""create table if not exists Students(
               s_no integer primary key,
               s_name text,
               s_email text,
               s_gender varchar,
               s_mobile integer
)
""")
conn.commit()
print("Table Created successfully!")

#insering the values
cursor.execute("insert into students (s_name, s_email, s_gender, s_mobile) values (?, ?, ?, ?)",
               ("Divya","divya@gmail.com","Female",6305078330))
cursor.execute("insert into students (s_name, s_email, s_gender, s_mobile) values (?, ?, ?, ?)",
               ("chitti","chitti@gmail.com","male",7865456789))
cursor.execute("insert into students (s_name, s_email, s_gender, s_mobile) values (?, ?, ?, ?)",
               ("cryso","cryso@gmail.com","Female",6456788330))
cursor.execute("insert into students (s_name, s_email, s_gender, s_mobile) values (?, ?, ?, ?)",
               ("cherry","cherry@gmail.com","male",9876543212))
cursor.execute("insert into students (s_name, s_email, s_gender, s_mobile) values (?, ?, ?, ?)",
               ("smiley","smiley@gmail.com","Female",5678987657))
conn.commit()
print("values inserted successfully!")

#To Display the data
cursor.execute("select * from students")
rows =cursor.fetchall()

print("\nDisplaying all Records:")
for row in rows:
    print(row)

#To close the connection
conn.close()