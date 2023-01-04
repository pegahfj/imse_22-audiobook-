insert_dummy = """
        INSERT INTO Users 
            (username, email, password)
        VALUES  
            ('playus0', 'wstruan0@constantcontact.com', 'KITmqdf1RbZ'),
            ('mchilver1', 'akeel1@umich.edu', 'jF6Jm0'),
            ('jnayshe2', 'kdowdle2@spotify.com', 'n7899bzcEo'),
            ('lvenediktov3', 'edutson3@pen.io', 'sI1y9kbXie'),
            ('thughs4', 'cessame4@yandex.ru', 'Llqr4HXG'),
            ('nbollard5', 'nbraitling5@addtoany.com', '64STOBQSP'),
            ('aalvarado6', 'mteliga6@mapy.cz', 's8jwdrkm');
        """

insert_dummy = """
    INSERT INTO AUDBOOKS
        (category_id, author_id, title, lang, rating)
    VALUES
        (1, 10, 'The Catcher in the Rye', 'English', 4),
        (2, 20, 'Nine Stories', 'English', 4),
        (3, 30, 'Franny and Zooey', 'English', 4),
        (4, 40, 'The Great Gatsby', 'English', 4),
        (5, 50, 'Tender id the Night', 'English', 4),
        (1, 60, 'Pride and Prejudice', 'English', 4),
        (2, 70, 'Professional ASP.NET 4.5 in C# and VB', 'English', 4);
    """

    find = """
    SELECT * FROM AUTHORS WHERE AUTHORS.auth_name iLIKE %s;
    """
    # {{ '%' + petId.value + '%' }}
    #  LIKE '%' || LOWER(tag_name) || '%';
    