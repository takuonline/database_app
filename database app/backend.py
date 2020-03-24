
#back end
import sqlite3

def connect():
    conn=sqlite3.connect("books.db")
    cursor=conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY,title text, author text, year integer, isbn integer)")
    conn.commit()
    conn.close()
    
def insert(title,author,year,isbn):
    conn=sqlite3.connect('books.db')
    cursor=conn.cursor()
    cursor.execute("INSERT INTO book VALUES (NULL,?,?,?,?)",(title,author,year,isbn))
    conn.commit()
    conn.close()

def view():
    conn=sqlite3.connect('books.db')
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM book")
    rows=cursor.fetchall()
    conn.close() 
    return rows

def delete(id_num):
    conn=sqlite3.connect('books.db')
    cursor=conn.cursor()
    cursor.execute("DELETE FROM book WHERE id=?", (id_num,))
    conn.commit()
    conn.close()
    
def search(title="",author="",year="",isbn=""):
    conn=sqlite3.connect('books.db')
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM book  WHERE title=? OR author=? OR year=? OR isbn=?",(title,author,year,isbn))
    rows=cursor.fetchall()
    conn.close()
    return rows


def update(id_num,title,author,year,isbn):
    conn=sqlite3.connect('books.db')
    cursor=conn.cursor()
    cursor.execute("UPDATE book SET title=?,author=?,year=?,isbn=? WHERE id=?", (title,author,year,isbn,id_num))
    conn.commit()
    conn.close()

connect()
#insert("the moon","taku",2020,38282092)


#print(search(author='taku'))    
#delete(4)
#update(5,'new book','napolean',1997,1234)
#print(view())




