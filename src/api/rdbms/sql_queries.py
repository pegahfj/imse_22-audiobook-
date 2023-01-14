class Create:
    author = """
    CREATE TABLE AUTHORS (
        id INTEGER GENERATED ALWAYS AS IDENTITY 
            (START WITH 10 INCREMENT BY 10) PRIMARY KEY,
        auth_name VARCHAR(255) NOT NULL,
        countryOforigins TEXT NOT NULL);"""

    audbook = """
    CREATE TABLE AUDBOOKS (
        id INTEGER GENERATED ALWAYS AS IDENTITY 
            (START WITH 10 INCREMENT BY 10) PRIMARY KEY,
        author_id INTEGER REFERENCES AUTHORS(id),
        title TEXT NOT NULL,
        year INTEGER,
        lang TEXT NOT NULL,
        rating INTEGER,
        dur INTEGER,
        images VARCHAR);"""

    user = """
     CREATE TABLE Users(
        id INTEGER GENERATED ALWAYS AS IDENTITY 
            (START WITH 10 INCREMENT BY 10) PRIMARY KEY,
        username TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        password TEXT CHECK (length(password) <= 500)  NOT NULL
    ); """

    collection = """
    CREATE TABLE COLLECTION (
        id INTEGER GENERATED ALWAYS AS IDENTITY 
            (START WITH 10 INCREMENT BY 10) PRIMARY KEY,
        user_id INTEGER REFERENCES USERS(id) UNIQUE
    );"""


    collection_book = """
    CREATE TABLE COLLECTIONB_BOOK (
        collection_id INTEGER REFERENCES collection(id),
        book_id INTEGER REFERENCES AUDBOOKS(id),
        PRIMARY KEY (collection_id, book_id)   
    );"""


class Drop:
    author = "DROP TABLE IF EXISTS authors CASCADE;"
    audbook = "DROP TABLE IF EXISTS audbooks CASCADE;"
    user = "DROP TABLE IF EXISTS users CASCADE;"
    collection = "DROP TABLE IF EXISTS COLLECTION CASCADE;"
    collection_book = "DROP TABLE IF EXISTS COLLECTIONB_BOOK CASCADE;"



class Join:
    books_authors = """
    CREATE TABLE BOOKAUTHOR AS 
    SELECT audbooks.title, authors.auth_name , audbooks.lang, audbooks.images
    FROM AUDBOOKS
    LEFT JOIN AUTHORS USING (id);"""
    
    collection_book =  """
    CREATE TABLE collection AS 
    SELECT user_collection.id, user_collection.user_id, collection_book.book_id
    FROM user_collection
    INNER JOIN collection_book ON id = collection_id;"""



class SingleInsert:
    author = """
    INSERT INTO AUTHORS (auth_name,countryOforigins)
    VALUES (%s, %s) RETURNING id;"""
    audbook = """
    INSERT INTO AUDBOOKS (author_id, title, year, lang, rating, dur, images)
    VALUES (%s, %s, %s, %s, %s, %s, %s);"""
    user = """
    INSERT INTO Users (username, email, password)
    VALUES (%s, %s, %s)  RETURNING id;"""


class Read:
    userID = """SELECT * FROM Users WHERE id = %s;"""
    userEmail = """SELECT * FROM Users WHERE email = %s;"""
    author = "SELECT * FROM AUTHORS;"
    authorID = """
    SELECT * FROM AUTHORS WHERE AUTHORS.id = %s;
    """
    authorName = """
    SELECT * FROM AUTHORS WHERE AUTHORS.auth_name iLIKE %s;
    """
    audbook = "SELECT * FROM AUDBOOKS"
    searchBar = "SELECT * FROM BOOKAUTHOR WHERE (BOOKAUTHOR.title iLIKE %s OR BOOKAUTHOR.auth_name iLIKE %s);"
   










