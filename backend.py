import sqlite3

def create():
    conn = sqlite3.connect("book_store.db")
    cur = conn.cursor()
    create_query = "CREATE TABLE IF NOT EXISTS books(title TEXT,author TEXT, isbn INT, year INT)"
    cur.execute(create_query)
    conn.commit()
    conn.close()

def display():
    conn = sqlite3.connect("book_store.db")
    cur = conn.cursor()
    select_query = "SELECT * FROM books"
    cur.execute(select_query)
    result = cur.fetchall()
    conn.close()
    return result

def insert(title,author,isbn,year):
    conn = sqlite3.connect("book_store.db")
    cur = conn.cursor()
    insert_query = "INSERT INTO books VALUES(?,?,?,?)"
    cur.execute(insert_query,(title,author,isbn,year))
    conn.commit()
    conn.close()


def delete(title):
    conn = sqlite3.connect("book_store.db")
    cur = conn.cursor()
    delete_query = "DELETE FROM books WHERE title = ?"
    cur.execute(delete_query,(title,))
    conn.commit()
    conn.close()

def search(title='',author = '', isbn = '', year = ''):
    conn = sqlite3.connect("book_store.db")
    cur = conn.cursor()
    search_query = "SELECT * FROM books WHERE title=? or author =? or isbn = ? or year = ?"
    cur.execute(search_query,(title,author,isbn,year))
    result = cur.fetchall()
    conn.close()
    return result

def update(author,isbn,year,title):
    conn = sqlite3.connect("book_store.db")
    cur = conn.cursor()
    update_query = "UPDATE books SET author = ?, isbn = ?, year = ? WHERE title = ?"
    cur.execute(update_query,(author,isbn,year,title))
    conn.commit()
    conn.close()

