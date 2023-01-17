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
        book_id INTEGER REFERENCES AUDBOOKS(id),
        user_id INTEGER REFERENCES USERS(id) 
    );"""
    
    bestseller =  """
    CREATE TABLE BestSeller AS 
    SELECT AUTHORS.id,  AUTHORS.auth_name, COUNT(AUDBOOKS.id)
    FROM COLLECTION
    JOIN AUDBOOKS ON COLLECTION.book_id = AUDBOOKS.id 
    JOIN AUTHORS ON AUDBOOKS.author_id = AUTHORS.id
    GROUP BY AUTHORS.id
    ORDER BY COUNT(AUDBOOKS.id) DESC;"""

    # collection_book = """
    # CREATE TABLE COLLECTIONB_BOOK (
    #     collection_id INTEGER REFERENCES collection(id),
    #     book_id INTEGER REFERENCES AUDBOOKS(id),
    #     PRIMARY KEY (collection_id, book_id)   
    # );"""


class Drop:
    author = "DROP TABLE IF EXISTS authors CASCADE;"
    audbook = "DROP TABLE IF EXISTS audbooks CASCADE;"
    user = "DROP TABLE IF EXISTS users CASCADE;"
    collection = "DROP TABLE IF EXISTS COLLECTION CASCADE;"
    bestseller = "DROP TABLE IF EXISTS bestseller CASCADE;"



class Join:
    books_authors = """
    CREATE TABLE BOOKAUTHOR AS 
    SELECT audbooks.title, authors.auth_name , audbooks.lang, audbooks.images
    FROM AUDBOOKS
    LEFT JOIN AUTHORS USING (id);"""
    
    



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
    collection = """
    INSERT INTO COLLECTION (book_id, user_id)
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
    audbook = "SELECT * FROM AUDBOOKS;"
    searchBar = "SELECT * FROM BOOKAUTHOR WHERE (BOOKAUTHOR.title iLIKE %s OR BOOKAUTHOR.auth_name iLIKE %s);"
    report = "SELECT * FROM BestSeller;"
#     report2 = """
#     CREATE TABLE BestSeller AS 
#     SELECT auth_name, AUTHORS.book_id
#     SELECT DISTINCT ON (b.id), b.*, SUM(oi.quantity) as total_quantity
#     FROM order_items oi JOIN
#         orders o
#         ON oi.order_id = o.id JOIN
#         books b
#         ON oi.book_id = b.id
#     WHERE o.status in (2, 3)
#     GROUP BY b.id
#     ORDER BY b.category_id, total_quantity DESC
# """
   










