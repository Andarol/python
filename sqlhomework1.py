import sqlite3


def query_to_display_names(connection):
    cur = connection.cursor()
    cur.execute('SELECT e.first_name as First_name,e.last_name as Last_name FROM employees as e')
    return cur.fetchall()


def query_uniq_deb_id(connection):
    cur = connection.cursor()
    cur.execute('SELECT DISTINCT e.department_id FROM employees as e')
    return cur.fetchall()


def all_details(connection):
    cur = connection.cursor()
    cur.execute('SELECT * FROM employees ORDER BY employees.first_name DESC')
    data = cur.fetchall()
    return data
def query_the_PF(connection):
    cur = connection.cursor()
    cur.execute('SELECT first_name,last_name,salary*0.12 FROM employees ')
    data = cur.fetchall()
    return data
def max_min(connection):
    cur = connection.cursor()
    cur.execute('SELECT MIN(salary),MAX(salary) FROM employees')
    return cur.fetchall()
def money(connection):
    cur = connection.cursor()
    cur.execute('SELECT ROUND(salary,2) FROM employees')
    return cur.fetchall()
#не розумію,або можливо у мене таблиця побита,бо середньої
# зп у мене нема замість salary має стояти Avg_Salary вле у мене NONE
if __name__ == '__main__':
    connection = sqlite3.connect("hw.db")
    sql_query = """SELECT name FROM sqlite_master  
      WHERE type='table';"""
    cursor = connection.cursor()
    cursor.execute(sql_query)
    print(cursor.fetchall())
    print('task1')
    print(query_to_display_names(connection))
    print('Task2')
    print(query_uniq_deb_id(connection))
    print('Task3')
    print(all_details(connection), sep='\n')
    print('task4')
    print(query_the_PF(connection))
    print('task5')
    print(max_min(connection))
    print('task6')
    print(money(connection))