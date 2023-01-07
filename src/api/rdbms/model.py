class Author():
    create = """
    CREATE TABLE AUTHORS (
        id INTEGER GENERATED ALWAYS AS IDENTITY 
            (START WITH 10 INCREMENT BY 10) PRIMARY KEY,
        auth_name VARCHAR(255) NOT NULL,
        countryOforigins TEXT NOT NULL);"""

    find_by_name = """
    SELECT * FROM AUTHORS WHERE AUTHORS.auth_name iLIKE %s;
    """
    
    find_by_id = """
    SELECT * FROM AUTHORS WHERE AUTHORS.id = %s;
    """
  
    insert_csv = """
    COPY Authors(auth_name,countryOforigins)
    FROM '/Users/pegah/Desktop/IMSE/submissions-22/M2/audiobooker2.0/Docs/authors.csv'
    DELIMITER ';'
    CSV HEADER;"""

    insert_one = """
    INSERT INTO AUTHORS (auth_name,countryOforigins)
    VALUES (%s, %s) RETURNING id;
    """


class Category():
    create = """
    CREATE TABLE CATEGORIES (
        id INTEGER GENERATED ALWAYS AS IDENTITY 
            (START WITH 1 INCREMENT BY 1) PRIMARY KEY,
        title TEXT CHECK (title IN ('Non-Fiction', 'Fiction', 'Sci-Fi', 'Thriller', 'Romance')) NOT NULL
    );"""

    insert = """
    INSERT INTO CATEGORIES
        (title)
    VALUES
        ('Non-Fiction'),
        ('Fiction'),
        ('Sci-Fi'),
        ('Thriller'),
        ('Romance');"""


class Audbook():
    create = """
    CREATE TABLE AUDBOOKS (
        id INTEGER GENERATED ALWAYS AS IDENTITY 
            (START WITH 10 INCREMENT BY 10) PRIMARY KEY,
        category_id INTEGER REFERENCES CATEGORIES(id),
        author_id INTEGER REFERENCES AUTHORS(id),
        title TEXT UNIQUE NOT NULL,
        lang TEXT CHECK (lang IN ('English', 'German', 'French', 'Spanish')) NOT NULL,
        -- dur TIME,
        rating INTEGER CHECK (rating between 0 and 5));"""

    create2 = """
    CREATE TABLE AUDBOOKS (
        id INTEGER GENERATED ALWAYS AS IDENTITY 
            (START WITH 10 INCREMENT BY 10) PRIMARY KEY,
        author_id INTEGER REFERENCES AUTHORS(id),
        title TEXT NOT NULL,
        year INTEGER,
        lang TEXT NOT NULL,
        images VARCHAR);"""

    insert_one = """
    INSERT INTO AUDBOOKS (author_id, title, year, lang, images)
    VALUES (%s, %s, %s, %s, %s);"""

    insert_csv = """
    COPY AUDBOOKS(author_id, title, year, lang,images)
    FROM '/Users/pegah/Desktop/IMSE/submissions-22/M2/audiobooker2.0/Docs/books.csv'
    DELIMITER ';'
    CSV HEADER;"""

    find = """
    SELECT * FROM AUDBOOKS WHERE AUDBOOKS.title iLIKE %s; 
    """
  

class User():
    create = """
     CREATE TABLE Users(
        id INTEGER GENERATED ALWAYS AS IDENTITY 
            (START WITH 10 INCREMENT BY 10) PRIMARY KEY,
        username TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        password TEXT CHECK (length(password) <= 500)  NOT NULL
    ); """

    insert = """
        INSERT INTO Users (username, email, password)
        VALUES (%s, %s, %s);"""
    
    find = """
    SELECT * FROM Users WHERE email = %s ;
    """

    update = """
    UPDATE Users
    SET username = %s
    WHERE email = %s;
    """

    remove = """
    """


class Subscription():
    create = """
    CREATE TABLE user_subscription (
        user_id INTEGER REFERENCES USERS(id) UNIQUE,
        subs_type INTEGER CHECK (subs_type IN (6, 12, 24)),
        created_on DATE NOT NULL,
        PRIMARY KEY (user_id)
    );"""


class Collection():
    create = """
    CREATE TABLE user_collection (
        id INTEGER GENERATED ALWAYS AS IDENTITY 
            (START WITH 10 INCREMENT BY 10) PRIMARY KEY,
        user_id INTEGER REFERENCES USERS(id) UNIQUE
    );"""


class CollectBook():
    create = """
    CREATE TABLE collection_book (
        collection_id INTEGER REFERENCES user_collection(id),
        book_id INTEGER REFERENCES AUDBOOKS(id),
        PRIMARY KEY (collection_id, book_id)   
    );"""
