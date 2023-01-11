import psycopg2
from psycopg2 import Error
from .model import User, Author, Category, Audbook, Subscription, Collection, CollectBook
import pandas as pd




class MyDB:
  def __init__(self, con):
    self.connection = con
    self.cursor  = self.connection.cursor()
    

  def session(self):       
      return self.cursor

  def init_db(self):
    self.clear_db()
    self.create_tables()
    self.insert_dummy_data()
    self.insert_book_fromCsv()
    self.books_authorsJoin()

  def clear_db(self):
    self.cursor.execute("DROP TABLE IF EXISTS authors CASCADE")
    self.cursor.execute("DROP TABLE IF EXISTS categories CASCADE")
    self.cursor.execute("DROP TABLE IF EXISTS audbooks CASCADE")
    self.cursor.execute("DROP TABLE IF EXISTS users CASCADE")
    self.cursor.execute("DROP TABLE IF EXISTS user_collection CASCADE")
    self.cursor.execute("DROP TABLE IF EXISTS collection_book CASCADE")
    self.cursor.execute("DROP TABLE IF EXISTS user_subscription CASCADE")
    self.cursor.execute("DROP TABLE IF EXISTS bookauthor CASCADE")
    self.connection.commit()

  def create_tables(self):
    self.cursor.execute(Author.create)
    self.cursor.execute(Category.create)
    self.cursor.execute(Audbook.create2)
    self.cursor.execute(User.create)
    self.cursor.execute(Subscription.create)
    self.cursor.execute(Collection.create)
    self.cursor.execute(CollectBook.create)
    self.connection.commit()

  def insert_dummy_data(self):
    self.cursor.execute(Author.insert_csv)
    self.cursor.execute(Category.insert)
    # self.cursor.execute(Audbook.insert_csv)
    # self.cursor.execute(Subscription.update)
    # self.cursor.execute(Collection.update)
    # self.cursor.execute(CollectBook.update)
    self.connection.commit()


# -----------------------------------------USER-----------------------------------------#

  def get_user_byId(self, user_id:int):
    find = """
    SELECT * FROM Users WHERE id = %s;"""
    self.cursor.execute(find, (user_id,))
    user = self.cursor.fetchone()
    if user != None:
        return list(user)
    else:
        return None


  def get_user_byEmail(self, email:str):
    find = """
    SELECT * FROM Users WHERE email = %s;"""
    self.cursor.execute(find, (email,))
    user = self.cursor.fetchone()
    if user != None:
        return list(user)
    else:
        return None


  def insert_single_user(self, username:str, email:str, password:str):
    insert = ("""
        INSERT INTO Users (username, email, password)
        VALUES (%s, %s, %s)  RETURNING id;""")
    
    if self.get_user_byEmail(email) != None:
        msg = 'E-Mail already exist'
    try:    
        var = (username, email, password)
        self.cursor.execute(insert, var)
        self.connection.commit()
        id_of_new_row = self.cursor.fetchone()[0]
        print(id_of_new_row) 
        return int(id_of_new_row)
    except:
        print(msg) 
  

  def update_user(self, new_username:str, email:str):
    update = """
    UPDATE Users
    SET username = %s
    WHERE email = %s;
    """
    val = (new_username, email)
    self.cursor.execute(update, val)
    self.connection.commit()



  # add a book to the collection of user
  def addTo_userCollection(self, user_id:int, book_id:int):
    find = """
    SELECT * FROM Users WHERE email = %s;"""
    self.cursor.execute(find, (email,))
    user = self.cursor.fetchone()

  # get the collection of user
  def get_userCollection(self, user_id:int):
    find = """
    SELECT * FROM Users WHERE email = %s;"""
    self.cursor.execute(find, (email,))
    user = self.cursor.fetchone()
    if user != None:
        return list(user)
    else:
        return None

# -----------------------------------------AUTHOR-----------------------------------------#

  def get_all_authors(self):
    self.cursor.execute( "SELECT * FROM AUTHORS")
    authors = self.cursor.fetchall()
    return authors
  
  def get_author_byId(self, id:int):
    self.cursor.execute(Author.find_by_id, (id,))
    author = self.cursor.fetchone()
    return author

  def get_author_byName(self, name:str):
    self.cursor.execute( Author.find_by_name , ('%' + name + '%',))
    author = self.cursor.fetchone()
    if author:
      return list(author)
    return None

  def insert_single_author(self, name:str, country:str):
    author = self.get_author_byName(name)
    if author:
      return author[0]
    else:
      val = (name, country)
      self.cursor.execute(Author.insert_one, val)
      self.connection.commit()
      id_of_new_row = self.cursor.fetchone()[0]
      return id_of_new_row


# -----------------------------------------AUDIOBOOK-----------------------------------------#
  
  def get_all_books(self):
    self.cursor.execute( "SELECT * FROM AUDBOOKS")
    self.connection.commit()
    books = self.cursor.fetchall()
    return books
  
  def insert_book_withAuthor(self, auth_name:str, country:str, title:str, year:int, lang:str):
    author_id = self.insert_single_author(auth_name, country)
    val = (author_id, title, year, lang)
    self.cursor.execute(Audbook.insert_one, val)
    self.connection.commit()

  def insert_single_book(self, auth_name:str, title:str, year:int, lang:str):
    author = self.get_author_byName(auth_name)
    author_id = author[0]
    val = (author_id, title, year, lang)
    self.cursor.execute(Audbook.insert_one, val)
    self.connection.commit()
  
  def insert_book_fromCsv(self):
# author_id, title, year, lang,images
    df = pd.read_csv(r'src/db/data/books.csv', sep=";")
    for index, row in df.iterrows():
      auth_name = row['auth_name'] 
      title = row['Title'] 
      year = row['Year'] 
      lang = row['Language'] 
      images = "images/"+row['images']
      author = self.get_author_byName(auth_name)
      author_id = author[0]
      val = (author_id, title, year, lang, images)
      self.cursor.execute(Audbook.insert_one, val)
      self.connection.commit()


# -----------------------------------------JOINS-----------------------------------------#

  def books_authorsJoin(self):
    quary = """
    CREATE TABLE BOOKAUTHOR AS 
    SELECT audbooks.title, authors.auth_name , audbooks.lang, audbooks.images
    FROM AUDBOOKS
    LEFT JOIN AUTHORS USING (id);"""
    self.cursor.execute( quary)
    self.connection.commit()



# -----------------------------------------GENERAL-----------------------------------------#

  def search_books(self, name:str):
    # SELECT * FROM BOOKAUTHOR WHERE BOOKAUTHOR.title OR BOOKAUTHOR.auth_name iLIKE %s; 
    quary = "SELECT * FROM BOOKAUTHOR WHERE (BOOKAUTHOR.title iLIKE %s OR BOOKAUTHOR.auth_name iLIKE %s);"
    val  = ('%' + name + '%', '%' + name + '%')
    self.cursor.execute( quary , val)
    book = self.cursor.fetchall()
    return book
# where 'Italy' IN (name, native, place);

  # def delete_table(self, table:str):
  #   self.cursor.execute("DROP TABLE IF EXISTS "+table)
  #   self.connection.commit()


# db = MyDB()
# if __name__ == "__main__":
#   pass