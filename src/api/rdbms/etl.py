from .sql_queries import Create, Drop, SingleInsert
import pandas as pd
import random


class ETLJobs:
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
    df = pd.read_csv(r'/Users/pegah/Desktop/IMSE/submissions-22/M2/audiobooker/src/api/rdbms/books.csv',header=0, sep=";", skiprows=lambda i: i>0 and random.random() > p)
    # df = pd.read_csv(r'src/db/data/books.csv', sep=";")
     
    for index, row in df.iterrows():
      auth_name = row['auth_name'] 
      auth_country = row['lang']
      val1 = (auth_name, auth_country)
      self.cursor.execute(SingleInsert.author, val1)
      self.connection.commit()
      authID = self.cursor.fetchone()[0]
     
      title = row['title'] 
      year = row['year'] 
      lang = row['lang'] 
      rating = row['rating'] 
      dur = row['dur'] 
      images = row['images'] 

      val2 = (authID, title, year, lang, rating, dur, images)
      self.cursor.execute(SingleInsert.audbook, val2)
      self.connection.commit()
     
     
     
    # for index, row in df.iterrows():
      # auth_name = row['auth_name'] 
      # title = row['Title'] 
      # year = row['Year'] 
      # lang = row['Language'] 
      # images = "images/"+row['images']
      # author = self.get_author_byName(auth_name)
      # author_id = author[0]
      # val = (author_id, title, year, lang, images)
      # self.cursor.execute(insert_one, val)
      # self.connection.commit()