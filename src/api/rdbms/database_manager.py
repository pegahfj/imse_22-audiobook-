from .sql_queries import Create, Drop, SingleInsert, Read
import pandas as pd
import random


class DatabaseManager:
  def __init__(self, con):
    self.connection = con
    self.cursor  = self.connection.cursor()


  def init_db(self):
    self.clear_db()
    self.create_tables()
    self.insert_bookCsv()

  def clear_db(self):
    self.cursor.execute(Drop.author)
    self.cursor.execute(Drop.audbook)
    self.cursor.execute(Drop.user)
    self.cursor.execute(Drop.collection)
    self.cursor.execute(Drop.collection_book)

    self.connection.commit()

  def create_tables(self):
    self.cursor.execute(Create.author)
    self.cursor.execute(Create.audbook)
    self.cursor.execute(Create.user)
    self.cursor.execute(Create.collection)
    self.cursor.execute(Create.collection_book)
    
    self.connection.commit()



     
  def insert_bookCsv(self):
    
# author_id, title, year, lang,images
    p = 0.1
    df = pd.read_csv(r'src/db/data/books.csv',header=0, sep=";", skiprows=lambda i: i>0 and random.random() > p)
    # df = pd.read_csv(r'src/db/data/books.csv', sep=";")
     
    for index, row in df.iterrows():
      auth_name = row['auth_name'] 
      auth_country = row['lang']
      authID = self.insert_author(auth_name, auth_country)
     
      title = row['title'] 
      year = row['year'] 
      lang = row['lang'] 
      rating = row['rating'] 
      dur = row['dur'] 
      images = "images/"+row['images'] 

      val = (authID, title, year, lang, rating, dur, images)
      self.cursor.execute(SingleInsert.audbook, val)
      self.connection.commit()
     
     
    

        # -----------------------------------------USER-----------------------------------------#


  def get_user_byId(self, user_id:int):
    self.cursor.execute(Read.userID, (user_id,))
    user = self.cursor.fetchone()
    if user != None:
        return list(user)
    else:
        return None


  
  def get_user_byEmail(self, email:str):
    self.cursor.execute(Read.userEmail, (email,))
    user = self.cursor.fetchone()
    if user != None:
        return list(user)
    else:
        return None



  def insert_single_user(self, username:str, email:str, password:str):  
    if self.get_user_byEmail(email) != None:
        msg = 'E-Mail already exist'
    try:    
        var = (username, email, password)
        self.cursor.execute(SingleInsert.user, var)
        self.connection.commit()
        id_of_new_row = self.cursor.fetchone()[0]
        print(id_of_new_row) 
        return int(id_of_new_row)
    except:
        print(msg) 


        # -----------------------------------------AUTHOR-----------------------------------------#

  def get_all_authors(self):
    self.cursor.execute(Read.author)
    authors = self.cursor.fetchall()
    return authors
  
  def get_author_byId(self, id:int):
    self.cursor.execute(Read.authorID, (id,))
    author = self.cursor.fetchone()
    return author

  def get_author_byName(self, name:str):
    self.cursor.execute(Read.authorName , ('%' + name + '%',))
    author = self.cursor.fetchone()
    if author:
      return list(author)
    return None

  def insert_author(self, name:str, country:str):
    author = self.get_author_byName(name)
    if author:
      return author[0]
    else:
      val = (name, country)
      self.cursor.execute(SingleInsert.author, val)
      self.connection.commit()
      id_of_new_row = self.cursor.fetchone()[0]
      return id_of_new_row
 

 # -----------------------------------------AUDIOBOOK-----------------------------------------#
  
  def get_all_books(self):
    self.cursor.execute(Read.audbook)
    self.connection.commit()
    books = self.cursor.fetchall()
    return books

 



# -----------------------------------------GENERAL-----------------------------------------#

  def search_books(self, name:str):
    val  = ('%' + name + '%', '%' + name + '%')
    self.cursor.execute(Read.searchBar , val)
    book = self.cursor.fetchall()
    return book