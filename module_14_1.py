# -*- coding: utf-8 -*-
import sqlite3

conn = sqlite3.connect("not_telegram.db")
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS Users")

# создание таблицы Users
sql = """CREATE TABLE IF NOT EXISTS Users (
id INTEGER PRIMARY KEY AUTOINCREMENT,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL)
"""
cursor.execute(sql)
conn.commit()

# заполнение 10 записями
for i in range(1, 11):
    sql = "INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)"
    cursor.execute(sql,(f"User{i}", f"example{i}@gmail.com", 10 * i, 1000))
conn.commit()

# обновление balance у каждой 2ой записи начиная с 1ой на 500
for i in range(1, 11, 2):
    sql = "UPDATE Users SET balance = 500 WHERE id = ?"
    cursor.execute(sql, (i,))
conn.commit()

# удаление каждой 3й записи в таблице начиная с 1ой:
for i in range(1, 11, 3):
    sql = "DELETE FROM Users WHERE id = ?"
    cursor.execute(sql, (i,))
conn.commit()

# выборка всех записей при помощи fetchall(), где возраст не равен 60
sql = "SELECT username, email, age, balance FROM Users WHERE age <> 60"
result = cursor.execute(sql).fetchall()
for username, email, age, balance in result:
    print(f"Имя: {username} | Почта: {email} | Возраст: {age} | Баланс: {balance}")
