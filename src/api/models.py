from src import db



class User:
    def __init__(self, username, email, password):
        self.id: int
        self.username: str = username
        self.email: str = email
        self.password: str = password
        # self.collection = UserCollection(self.id)

    # @classmethod
    # def get_instance(cls, user:list):
    #     return User(user[0], user[1], user[2], user[3])

    def set_id(self, id):
        self.id = id

    def validate_email(email:str):
        exist_email = False
        user = db.get_user_byEmail(email)
        if user:
            exist_email = True  
        return exist_email

         
    def get_byID(user_id:int):
        user = db.get_user_byId(user_id)
        if user:
            return User.get_instance(user)
        return None

      
    def get_byEmail(email:str):
        user = db.get_user_byEmail(email)
        if user:
            return User.get_instance(user)
        return None
    
    def get_all():
        return db.get_all_users()
    
    # def insert(user, email, passw):
    #         o = db.insert_single_user(user, email, passw)
    #         if type(o) is int:
    #             return o
    #         else:
    #             return None

    # def get_collection(self, user_id):
    #      self.collection 


    # def update_user(self, new_username:str, email:str):
    #     db.update_user(new_username, email)
     
                
    # def __repr__(self):
    #     return f"User('{self.username}', '{self.email}', '{self.password}')"




   
    def add_book(self, book_id):
            db.addTo_userCollection( self.user_id, book_id)
            

class Book():
    def __init__(self, title:str, year:int, language:str):
        self.id: int 
        self.author_id: int 
        self.title: str = title
        self.year: int = year
        self.lang: str = language    
     



class UserCollection:
    def __init__(self, id):
        self.user_id = id
        self.books = list() 
        
    
    def get_books(self):
        col = db.get_userCollection(self.user_id)
        if col:
            for book in col:
                self.books.append(list(book))
            return self.books
        return None