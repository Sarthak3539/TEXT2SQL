import sqlite3

connection = sqlite3.connect('database.db')
cursor = connection.cursor()

# Create Department table
cursor.execute("""
CREATE TABLE Department (
    ID INTEGER PRIMARY KEY,
    name TEXT,
    leadPersonID INTEGER,
    FOREIGN KEY (leadPersonID) REFERENCES Person(ID)
)
""")

# Create Project table
cursor.execute("""
CREATE TABLE Project (
    ID INTEGER PRIMARY KEY,
    title TEXT,
    startDate DATE,
    endDate DATE,
    departmentID INTEGER,
    FOREIGN KEY (departmentID) REFERENCES Department(ID)
)
""")

# Create Person table (removed entityID, added name)
cursor.execute("""
CREATE TABLE Person (
    ID INTEGER PRIMARY KEY,
    name TEXT,
    dayOfBirth DATE
)
""")

# Create Project_Members table
cursor.execute("""
CREATE TABLE Project_Members (
    projectID INTEGER,
    personID INTEGER,
    role TEXT,
    FOREIGN KEY (projectID) REFERENCES Project(ID),
    FOREIGN KEY (personID) REFERENCES Person(ID),
    PRIMARY KEY (projectID, personID)
)
""")

# Create Department_Members table
cursor.execute("""
CREATE TABLE Department_Members (
    departmentID INTEGER,
    personID INTEGER,
    FOREIGN KEY (departmentID) REFERENCES Department(ID),
    FOREIGN KEY (personID) REFERENCES Person(ID),
    PRIMARY KEY (departmentID, personID)
)
""")


# Insert data into Department table
departments_data = [
    (1, 'Machine Learning', 1),
    (2, 'Data Science', 2),
    (3, 'Software Development', 3),
    (4, 'Cyber Security', 4),
    (5, 'Cloud Computing', 5)
]

# Insert data into Project table
projects_data = [
    (1, 'ML Project 1', '2022-01-01', '2022-12-31', 1),
    (2, 'ML Project 2', '2023-01-01', '2023-12-31', 1),
    (3, 'DS Project 1', '2022-02-01', '2022-11-30', 2),
    (4, 'DS Project 2', '2023-02-01', '2023-11-30', 2),
    (5, 'DS Project 3', '2023-03-01', '2023-12-15', 2),
    (6, 'SD Project 1', '2022-03-01', '2022-10-31', 3),
    (7, 'SD Project 2', '2023-03-01', '2023-10-31', 3),
    (8, 'CS Project 1', '2022-04-01', '2022-09-30', 4),
    (9, 'CS Project 2', '2023-04-01', '2023-09-30', 4),
    (10, 'CC Project 1', '2022-05-01', '2022-08-31', 5),
    (11, 'CC Project 2', '2023-05-01', '2023-08-31', 5),
]

# Insert data into Person table
persons_data = [
    (1, 'Alice Johnson', '1980-05-15'),
    (2, 'Bob Smith', '1981-06-20'),
    (3, 'Charlie Davis', '1982-07-25'),
    (4, 'David Wilson', '1983-08-30'),
    (5, 'Emma Moore', '1984-09-05'),
    (6, 'Fiona Brown', '1985-10-10'),
    (7, 'George Clark', '1986-11-15'),
    (8, 'Hannah Harris', '1987-12-20'),
    (9, 'Ian Martin', '1988-01-25'),
    (10, 'Jack Lewis', '1989-02-28'),
    (11, 'Katie Walker', '1990-03-05'),
    (12, 'Liam Robinson', '1991-04-10'),
    (13, 'Mia Lee', '1992-05-15'),
    (14, 'Noah Young', '1993-06-20'),
    (15, 'Olivia King', '1994-07-25'),
    (16, 'Paul Scott', '1995-08-30'),
    (17, 'Quinn White', '1996-09-05'),
    (18, 'Rachel Hall', '1997-10-10'),
    (19, 'Sam Green', '1998-11-15'),
    (20, 'Tina Adams', '1999-12-20')
]

# Insert data into Project_Members table
project_members_data = [
    (1, 1, 'Lead'),
    (1, 2, 'Member'),
    (1, 3, 'Member'),
    (2, 4, 'Lead'),
    (2, 5, 'Member'),
    (2, 6, 'Member'),
    (2, 7, 'Member'),
    (3, 8, 'Lead'),
    (3, 9, 'Member'),
    (3, 10, 'Member'),
    (3, 11, 'Member'),
    (4, 12, 'Lead'),
    (4, 13, 'Member'),
    (4, 14, 'Member'),
    (5, 15, 'Lead'),
    (5, 16, 'Member'),
    (5, 17, 'Member'),
    (6, 18, 'Lead'),
    (6, 19, 'Member'),
    (6, 20, 'Member'),
    (7, 1, 'Lead'),
    (7, 2, 'Member'),
    (8, 3, 'Lead'),
    (8, 4, 'Member'),
    (9, 5, 'Lead'),
    (9, 6, 'Member'),
    (9, 7, 'Member'),
    (10, 8, 'Lead'),
    (10, 9, 'Member'),
    (11, 10, 'Lead'),
    (11, 11, 'Member'),
    (11, 12, 'Member')
]

# Insert data into Department_Members table
department_members_data = [
    (1, 1),
    (1, 2),
    (1, 3),
    (2, 4),
    (2, 5),
    (2, 6),
    (3, 7),
    (3, 8),
    (4, 9),
    (4, 10),
    (5, 11),
    (5, 12),
    (5, 13)
]

# Insert data into tables
for data in departments_data:
    cursor.execute('INSERT INTO Department VALUES (?, ?, ?)', data)

for data in projects_data:
    cursor.execute('INSERT INTO Project VALUES (?, ?, ?, ?, ?)', data)

for data in persons_data:
    cursor.execute('INSERT INTO Person VALUES (?, ?, ?)', data)

for data in project_members_data:
    cursor.execute('INSERT INTO Project_Members VALUES (?, ?, ?)', data)

for data in department_members_data:
    cursor.execute('INSERT INTO Department_Members VALUES (?, ?)', data)

Commit the changes and close the connection

data=cursor.execute(''' SELECT count(*) from Person

                  ''')

for x in data:
    print(x)

connection.commit()
connection.close()
