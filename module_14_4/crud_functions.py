# -*- coding: utf-8 -*-
import sqlite3


def initiate_db():
    conn = sqlite3.connect("not_telegram.db")
    cursor = conn.cursor()
    sql = """CREATE TABLE IF NOT EXISTS Products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT,
    price INTEGER NOT NULL
    );"""
    cursor.execute(sql)
    conn.commit()
    conn.close()


def get_all_products():
    conn = sqlite3.connect("not_telegram.db")
    conn.row_factory = sqlite3.Row
    res = conn.cursor().execute("SELECT * FROM Products").fetchall()
    conn.close()
    return res


if __name__ == "__main__":
    initiate_db()
    result = get_all_products()
    for product in result:
        print(dict(product))
