import sqlite3


def connect():
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book1 (id INTEGER PRIMARY KEY, title TEXT, author TEXT, genre TEXT,"
                " year INT, isbn INT, mark INT)")
    conn.commit()
    conn.close()


def insert(title, author, genre, year, isbn, mark):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO book1 VALUES (NULL, ?,?,?,?,?,?)", (title, author, genre, year, isbn, mark))
    conn.commit()
    conn.close()


def view():
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book1")
    rows = cur.fetchall()
    conn.close()
    return rows


def search(title="", author="", genre="", year="", isbn="", mark=""):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book1 WHERE title = ? OR author = ? OR genre = ? OR year = ? OR isbn = ? OR mark = ?",
                (title, author, genre, year, isbn, mark))
    rows = cur.fetchall()
    conn.close()
    return rows


def delete(id):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM book1 WHERE id = ?", (id,))
    conn.commit()
    conn.close()


def update(id, title, author, genre, year, isbn, mark):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("UPDATE book1 SET title = ?, author = ?, genre = ?, year = ?, isbn = ?, mark = ? WHERE id = ?",
                (title, author, genre, year, isbn, mark, id))
    conn.commit()
    conn.close()


connect()