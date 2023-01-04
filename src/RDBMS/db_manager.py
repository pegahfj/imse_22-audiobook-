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
    self.insert_csv_book()
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

  def get_user(self, email:str):
    self.cursor.execute(User.find, (email,))
    user = self.cursor.fetchone()
    if user:
      return list(user)
    return None

  def validate_email(self, email:str):
    exist_email: bool = False
    self.cursor.execute(User.find, (email,))
    user = self.cursor.fetchone()
    if user:
      exist_email = True  
    return exist_email

  def insert_user(self, username:str, email:str, password:str):
    # is_user: bool = False
    # id_list = self.get_user(email)
    # if len(id_list) > 0:
    #   is_user = True
    #   return is_user
    # else:
    val = (username, email, password)
    self.cursor.execute(User.insert, val)
    self.connection.commit()
      # return is_user
  
  def update_user(self, new_username:str, email:str):
    val = (new_username, email)
    self.cursor.execute(User.update, val)
    self.connection.commit()


# -----------------------------------------AUTHOR-----------------------------------------#

  def get_authors(self):
    self.cursor.execute( "SELECT * FROM AUTHORS")
    authors = self.cursor.fetchall()
    return authors
  
  def get_author_name(self, id:int):
    self.cursor.execute(Author.find_by_id, (id,))
    author = self.cursor.fetchone()
    return author

  def find_author(self, name:str):
    self.cursor.execute( Author.find_by_name , ('%' + name + '%',))
    author = self.cursor.fetchone()
    if author:
      return list(author)
    return None

  def insert_author(self, name:str, country:str):
    author = self.find_author(name)
    if author:
      return author[0]
    else:
      val = (name, country)
      self.cursor.execute(Author.insert_one, val)
      self.connection.commit()
      id_of_new_row = self.cursor.fetchone()[0]
      return id_of_new_row


# -----------------------------------------AUDIOBOOK-----------------------------------------#
  
  def get_books(self):
    self.cursor.execute( "SELECT * FROM AUDBOOKS")
    self.connection.commit()
    books = self.cursor.fetchall()
    return books
  
  def insert_book_author(self, auth_name:str, country:str, title:str, year:int, lang:str):
    author_id = self.insert_author(auth_name, country)
    val = (author_id, title, year, lang)
    self.cursor.execute(Audbook.insert_one, val)
    self.connection.commit()

  def insert_book(self, auth_name:str, title:str, year:int, lang:str):
    author = self.find_author(auth_name)
    author_id = author[0]
    val = (author_id, title, year, lang)
    self.cursor.execute(Audbook.insert_one, val)
    self.connection.commit()
  
  def insert_csv_book(self):
# author_id, title, year, lang,images
    df = pd.read_csv(r'Docs/books.csv', sep=";")
    for index, row in df.iterrows():
      auth_name = row['auth_name'] 
      title = row['Title'] 
      year = row['Year'] 
      lang = row['Language'] 
      images = "images/"+row['images'] 
      author = self.find_author(auth_name)
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