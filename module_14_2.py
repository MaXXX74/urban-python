# -*- coding: utf-8 -*-
import sqlite3

conn = sqlite3.connect("not_telegram.db")
cursor = conn.cursor()

# удаление из базы данных not_telegram.db запись с id = 6
cursor.execute("DELETE FROM Users WHERE id = 6")
conn.commit()

# подсчитываем общее количество записей
total_users = cursor.execute("SELECT COUNT(*) FROM Users").fetchone()[0]

# рассчитываем сумму всех балансов
all_balances = cursor.execute("SELECT SUM(balance) FROM Users").fetchone()[0]

# вывод в консоль среднего баланса всех пользователей
print(all_balances / total_users)

conn.close()
