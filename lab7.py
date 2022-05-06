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
    print("""Виберіть дію 
        1. Вийти
         2.Створити новий обліковий запис
         3.Створити завдання
         4.Видалити завдання
         5.Змінити завдання
         6.Перевірте список завдань
        """)
    user_input = input("Для вибору дії надрукуйте його номер: ")
    return user_input


def reg():
    user_login = input("Логін: ")
    user_password = input("Пароль: ")
    user_task = ''
    sql.execute(f"SELECT task FROM tasks WHERE task = '{user_task}'")
    if sql.fetchone() is None:
        sql.execute(f"INSERT INTO tasks VALUES (?)", (user_task,))
        db.commit()
        print("Поле завдання створено")
    sql.execute(f"SELECT login FROM users WHERE login = '{user_login}'")
    if sql.fetchone() is None:
        sql.execute(f"INSERT INTO users VALUES (?, ?)", (user_login, user_password))
        db.commit()
        print("Реєстрацію завершено успішно!")
    else:
        print("Той самий обліковий запис уже створено!")
    for value in sql.execute("SELECT * FROM users"):
        print(value)
    for value in sql.execute("SELECT * FROM tasks"):
        print(value)


def login():
    user_login = input("Логін: ")
    user_password = input("Пароль: ")

    sql.execute(f"SELECT login FROM users WHERE login = '{user_login}'")
    if sql.fetchone() is None:
        print("Неправильний логін або пароль!")
        user_action = input("Ви хочете створити новий обліковий запис? (print 'y' or 'n')")
        if user_action == 'y':
            reg()
        else:
            False
    else:
        print("Вхід виконано!")
        return start_action()


def task_action(action):
    if action == "add":
        user_task = input("Надрукуйте назву завдання: ")
        sql.execute(f"INSERT INTO tasks VALUES (?)", (user_task,))
        db.commit()
    elif action == "delete":
        user_task = input("Надрукуйте назву завдання, яке потрібно видалити: ")
        sql.execute(f"DELETE FROM tasks WHERE task = '{user_task}'")
        db.commit()
        print("Завдання видалено")
    elif action == "change":
        user_task = input("Надрукуйте назву завдання: ")
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
