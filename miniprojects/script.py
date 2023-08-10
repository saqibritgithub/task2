import sqlite3

# Connect to the database (or create it if it doesn't exist)
conn = sqlite3.connect("usama_database.db")
conn.execute('''
         create table students(
         st_id INT AUTO_INCREMENT PRIMARY KEY,
         st_name VARCHAR(50),
         st_class VARCHAR(10),
         st_email VARCHAR(30)
         )
          
    ''')
conn.close()

