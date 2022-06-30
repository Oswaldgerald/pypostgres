import psycopg2


# establishing the connection
def create():
    conn = psycopg2.connect(database="studentdb", user='postgres', password='postgres', host='localhost', port='5433')
    cur = conn.cursor()
    cur.execute('''CREATE TABLE student(ID SERIAL,NAME TEXT,AGE TEXT,ADDRESS TEXT);''')
    print('print connection success')
    conn.commit()
    conn.close()


def insert_data():
    conn = psycopg2.connect(database="studentdb", user='postgres', password='postgres', host='localhost', port='5433')
    cur = conn.cursor()
    name = input('Enter your name')
    age = input('Enter your age')
    address = input('Enter your address')
    query = '''INSERT INTO student(NAME,AGE,ADDRESS) VALUES(%s,%s, %s);'''
    cur.execute(query, (name, age, address))
    print('Data submitted successfully')
    conn.commit()
    conn.close()


insert_data()
