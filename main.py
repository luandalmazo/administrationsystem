import sqlite3 #LIBRARY THAT PROVIDES A SQL DATABASE ENGINE

GERAL_PASSWORD = "0900" #THIS PASSWORD IS JUST FOR EXAMPLE, IT IS RECOMMENDED THAT YOU HAVE ENCRYPTED PASSWORDS

password = input("PLEASE ENTER YOUR PASSWORD: ") #LOGIN PROCESS
if password != GERAL_PASSWORD:
    print("SORRY, BUT YOUR PASSWORD DOESN'T APPEAR IN OUR SYSTEM!")
    exit()

conn = sqlite3.connect('system.db') #MAKING THE CONNECTION WITH THE DATABASE
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS employees (
    setor TEXT NOT NULL, username TEXT NOT NULL, password TEXT NOT NULL);''') #RESPONSIBLE FOR CREATE A TABLE IN THE DATABASE

def geral_menu(): #LIST ALL THE OPTIONS
    print("-----------------------------")
    print("i: INSERT A NEW EMPLOYEE")
    print("l: LIST ALL EMPLOYEES")
    print("d: DELETE A EMPLOYEE")
    print("e: EDIT A EMPLOYEE DATA")
    print("f: FINISH")

def show_employee(setor):
    cursor.execute(f'''SELECT setor,username FROM employees WHERE setor = 
    '{setor}' ''') #RESPONSIBLE FOR DOING A SEARCH IN THE DATABASE

    if cursor.rowcount == 0:
        print("EMPLOYEE NOT REGISTERED ")
    else:
        for employee in cursor.fetchall():
            print(employee)

def insert_employee(setor, username, password): #RESPONSIBLE FOR DOING AN INSERT OF A NEW EMPLOYEE IN THE DATABASE
    cursor.execute(f'''INSERT INTO employees (setor, username, password) VALUES
    ('{setor}','{username}','{password}')''')
    conn.commit()

def delete_employee(): #RESPONSIBLE FOR REMOVING AN EMPLOYEE FROM THE DATABASE
    cursor.execute(f'''SELECT * FROM employees ''')
    if cursor.rowcount == 0:
        print("NOT TO SEE HERE ")
    else:
        for employee in cursor.fetchall():
            print(employee)
    n = input(("ENTER A NAME TO DELETE: "))
    cursor.execute(f'''DELETE FROM employees WHERE username = '{n}' ''')
    if cursor.rowcount == 0:
        print("NOT TO SEE HERE ")
    else:
        for employee in cursor.fetchall():
            print(employee)

def edit_employee(): #RESPONSIBLE FOR EDIT A EMPLOYEE DATA
    n = input("TYPE A NAME TO EDIT: ")
    old = n
    cursor.execute(f'''SELECT setor,username FROM employees WHERE username = 
    '{n}' ''')
    n = input("TYPE THE NEW NAME: ")
    cursor.execute(f'''UPDATE employees SET username = '{n}' WHERE username = '{old}' ''' )


    if cursor.rowcount == 0:
        print("EMPLOYEE NOT REGISTERED ")
    else:
        for employee in cursor.fetchall():
            print(employee)
    

while True:
    geral_menu()
    choice = input("MY CHOICE: ")
    while choice not in ['i','l','d','e','f']:
        print("OPÇÃO INVALIDA")
        choice = input("MY CHOICE: ")

    if choice == 'i':
        s = input("TYPE THE SETOR OF THE EMPLOYEE: ")
        u = input("TYPE THE NAME OF THE EMPLOYEE: ")
        p = input("TYPE THE PASSWORD OF THE EMPLOYEE: ")
        insert_employee(s,u,p)

    if choice == 'l':
        s = input("TYPE THE SETOR OF THE EMPLOYEE: ")
        show_employee(s)
    
    if choice == 'd':
        delete_employee()

    if choice == 'e':
        edit_employee()
        
    if choice == 'f':
        break
    
conn.close() #RESPONSIBLE FOR CLOSING THE CONNECTION