import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
connection = sqlite3.connect('database.db')
cursor = connection.cursor()

# Create 'user' table
cursor.execute('''
CREATE TABLE IF NOT EXISTS user (
    id INTEGER PRIMARY KEY,
    first_name VARCHAR,
    last_name VARCHAR,
    middle_initial VARCHAR,
    address VARCHAR,
    city VARCHAR,
    state VARCHAR,
    zip VARCHAR,
    phone VARCHAR,
    email VARCHAR,
    tagline TEXT
)
''')

# Create 'courses' table
cursor.execute('''
CREATE TABLE IF NOT EXISTS courses (
   course_number INTEGER PRIMARY KEY ,
   name VARCAHR ,  
   description VARCAHR   
)
''')

# Create 'skills' table
cursor.execute('''
CREATE TABLE IF NOT EXISTS skills (
   skills_id INTEGER PRIMARY KEY ,
   skill_keyword VARCAHR    
)
''')

# Create 'course_skills' table
cursor.execute('''
CREATE TABLE IF NOT EXISTS course_skills (
   course_number INTEGER PRIMARY KEY ,
   skills_id INTEGER   
)
''')

# Create 'work_history' table
cursor.execute('''
CREATE TABLE IF NOT EXISTS work_history (
    work_id INTEGER PRIMARY KEY, 
    user_id INTEGER, 
    company_name VARCHAR, 
    address VARCHAR, 
     city 	VARCHAR, 
     state 	VARCHAR, 
     zip 	VARCHAR, 
     phone 	VARCHAR, 
     start_date DATE, 
     end_date DATE
)
''')

# Create 'jobs' table
cursor.execute('''
CREATE TABLE IF NOT EXISTS jobs (
 job_id	INTEGER	PRIMARY KEY ,	
 company_name	VARCHAR ,	
 address	VARCHAR ,	
 salary_range	VARCHAR ,	
 description	VARCHAR ,	
 hyperlink	VARCHAR ,	
 user_id	INTEGER    
 )
 ''')

# Create 'user_courses' table
cursor.execute('''
CREATE TABLE IF NOT EXISTS user_courses (
   user_id INTEGER PRIMARY KEY ,
   course_number INTEGER  
)
''')

connection.commit()
connection.close()
