import sqlite3

def create():
    conn = sqlite3.connect("store.db")
    cur = conn.cursor()
    create_query = "CREATE TABLE IF NOT EXISTS stores(store_id INT PRIMARY KEY, store_name TEXT)"
    create_query1 = "CREATE TABLE IF NOT EXISTS items(item_id INT, item_name TEXT, item_value TEXT, FOREIGN KEY(item_id) REFERENCES stores(store_id))"
    cur.execute(create_query)
    cur.execute(create_query1)
    conn.commit()
    conn.close()


def insert_store(store_id, store_name):
    conn = sqlite3.connect("store.db")
    cur = conn.cursor()
    insert_query = "INSERT INTO stores VALUES(?,?)"
    cur.execute(insert_query,(store_id,store_name))
    conn.commit()
    conn.close()

def insert_item(item_id,item_name,item_value):
    conn = sqlite3.connect("store.db")
    cur = conn.cursor()
    insert_query = "INSERT INTO items VALUES(?,?,?)"
    cur.execute(insert_query,(item_id,item_name,item_value))
    conn.commit()
    conn.close()

def select():
    conn = sqlite3.connect("store.db")
    cur = conn.cursor()
    select_query = "SELECT * FROM stores INNER JOIN items on store_id=item_id "
    cur.execute(select_query)
    result = cur.fetchall()
    conn.close()
    return result

def search(store_name=''):
    conn = sqlite3.connect("store.db")
    cur = conn.cursor()
    search_query = "SELECT * FROM stores WHERE store_name=?"
    cur.execute(search_query,(store_name))
    result = cur.fetchall()
    conn.close()
    return result

def update_store(store_name,store_id):
    conn = sqlite3.connect("store.db")
    cur = conn.cursor()
    update_query = "UPDATE stores SET store_name = ? where store_id = ?"
    cur.execute(update_query,(store_name,store_id))
    conn.commit()
    conn.close()


def update_item(item_name,item_value,item_id):
    conn = sqlite3.connect("store.db")
    cur = conn.cursor()
    update_query = "UPDATE items SET item_name=?, item_value=? where item_id=?"
    cur.execute(update_query,(item_name,item_value,item_id))
    conn.commit()
    conn.close()



print(select())


