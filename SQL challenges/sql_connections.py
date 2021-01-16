# Connect to MySQL
import mysql.connector
from mysql.connector import Error
import pandas as pd
import csv

def create_server_connection(host_name, user, user_pwd):
    connection = None

    try: 
        conn = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password
        )
        print("MySQL database connection successful")

    except:
        print('Error')

    return connection


def create_database(conn, query):
    curs = conn.cursor()
    try:
        curs.execute(query)
        print("Database created!")
    except:
        print("Error")

def execute_query(conn, query):
    curs = conn.cursor()
    try:
        curs.execute(query)
        conn.commit()
        print("Query successful!")
    except:
        print("Error")


    connection = create_server_connection(
        "hrfasylum-database-a.catpmmwmrkhp.us-east-1.rds.amazonaws.com", 
        "hrfasyluma", 
        "Monkey39")

    create_db_query = "CREATE DATABASE schools;"

    create_database(connection, query)

    create_teacher_table = """
    CREATE TABLE teacher (
        teacher_id INT PRIMARY KEY,
        first_name VARCHAR(30) NOT NULL,
        dob DATE,
        tax_id INT UNIQUE,
        phone_no VARCHAE(20),
        in_school BOOLEAN,
        phone_no VARCHAR(20)
    );
    """
    create_participant_table = """
    CREATE TABLE participant (
        participant_id INT PRIMARY KEY,
        first_name VARCHAR(30) NOT NULL,
        last_name VARCHAR(30) NOT NULL, 
        client INT
    );
    """

    execute_query(connection, create_teacher_table) 

    alter_participant_table = """ (
        ALTER TABLE participant
        ADD FOREIGN KEY(client)
        REFERENCES client(client_id)
        ON DELETE SET NULL
    );
    """

    alter_course_table = """ (
        ALTER TABLE course
        ADD FOREIGN KEY(teacher)
        REFERENCES teacher(teacher_id)
        ON DELETE SET NULL
    );"""

    alter_course_again = """
        ALTER TABLE course
        ADD FOREIGN KEY(client)
        REFERENCES client(client_id)
        ON DELETE SET NULL
        );
        """

    create_takescourse_table = """
    CREATE TABLE takes_course (
        participant_id INT,
        course_id INT,
        PRIMARY KEY(participant_id, course_id),
        FOREIGN KEY(participant_id) REFERENCES participant(participant_id) ON DELETE CASCADE,
        FOREIGN KEY(course_id) REFERENCES course(course_id) ON DELETE CASCADE
    );"""

    populate_teacher = """
    INSERT INTO teacher VALUES
    ()
    """


def insert_data_int_db(conn, csv):
    
    with open("tester.csv", 'rb') as f:
        csv_data = csv.reader(f, delimiter=',')
    
    with conn.cursor() as cur:
        for row in csv_data: 
            cur.execute('INSERT INTO schools.teacher(teacher_id, first_name, dob)' 'VALUES(%s, %s, %s)', row)
            conn.commit()

    # alternative way

    for i, row in irisData.itertuples():
        with conn.cursor() as cur:
            sql = "INSERT INTO schools.teacher VALUES (%s, %s)"
            data = (row.first_name, row.last_name)
            cur.execute(sql, data)


def read_query(conn, query):
    result = None

    try:
    
        cur = conn.cursor()
        cur.execute(query)
        result = cur.fetchall()
    except:
        print('Error')

conn = create_db_connection(host, user_name, pwd)

query = """SELECT * FROM teacher;"""
results = read_query(conn, query)

for result in results:
    print(result)

from_db = []

for result in results:
    result = list(result)
    from_db.append(result)


# into df
columns=['course_id', 'address']
df = pd.DataFrame(from_db, columns=columns)


