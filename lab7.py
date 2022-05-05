import sqlite3
import sys


global db
global sql
db = sqlite3.connect('accounts')
sql = db.cursor()
sql.execute("""CREATE TABLE IF NOT EXISTS users (
    login TEXT,
    password TEXT
)""")
db.commit()
sql.execute("""CREATE TABLE IF NOT EXISTS tasks (
    task TEXT
)""")
db.commit()


def start_action():
    print("""Choose you action 
        1.Log out
        2.Create new account
        3.Create task
        4.Delete task
        5.Change task
        6.Check the list of tasks
        """)
    user_input = input("For choosing you action print number of him: ")
    return user_input


def reg():
    user_login = input("Login: ")
    user_password = input("Password: ")
    user_task = ''
    sql.execute(f"SELECT task FROM tasks WHERE task = '{user_task}'")
    if sql.fetchone() is None:
        sql.execute(f"INSERT INTO tasks VALUES (?)", (user_task,))
        db.commit()
        print("Task field created")
    sql.execute(f"SELECT login FROM users WHERE login = '{user_login}'")
    if sql.fetchone() is None:
        sql.execute(f"INSERT INTO users VALUES (?, ?)", (user_login, user_password))
        db.commit()
        print("Registration done!")
    else:
        print("Same account already created!")
    for value in sql.execute("SELECT * FROM users"):
        print(value)
    for value in sql.execute("SELECT * FROM tasks"):
        print(value)


def login():
    user_login = input("Login: ")
    user_password = input("Password: ")

    sql.execute(f"SELECT login FROM users WHERE login = '{user_login}'")
    if sql.fetchone() is None:
        print("Wrong login or password!")
        user_action = input("Do you wanna create new account? (print 'y' or 'n')")
        if user_action == 'y':
            reg()
        else:
            False
    else:
        print("Login done!")
        return start_action()


def task_action(action):
    if action == "add":
        user_task = input("Print the task name: ")
        sql.execute(f"INSERT INTO tasks VALUES (?)", (user_task,))
        db.commit()
    elif action == "delete":
        user_task = input("Print the task name that you need to delete: ")
        sql.execute(f"DELETE FROM tasks WHERE task = '{user_task}'")
        db.commit()
        print("Task deleted")
    elif action == "change":
        user_task = input("Print the task name: ")
        sql.execute(f"UPDATE tasks SET task = '{user_task}'")
        db.commit()
    elif action == "check":
        for value in sql.execute("SELECT * FROM tasks"):
            print(value)


def user_actions(user_input):
    if user_input == "1":
        sys.exit()
    elif user_input == "2":
        reg()
    elif user_input == "3":
        task_action("add")
    elif user_input == "4":
        task_action("delete")
    elif user_input == "5":
        task_action("change")
    elif user_input == "6":
        task_action("check")


def main():
    user_actions(login())


main()
