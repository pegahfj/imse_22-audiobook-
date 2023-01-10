
from src import db

class Book():
    def __init__(self, title:str, year:int, language:str):
        self.id: int 
        self.author_id: int 
        self.title: str = title
        self.year: int = year
        self.lang: str = language


    def insert(self):
        o = db.insert_single_user(self.username, self.email, self.password)
        if type(o) is int:
            self.id = o
            return self.id 
        else:
            return None
    
      
    def get_user(self, email:str):
        user = db.get_user_byEmail(email)
        if user:
            # print(list(user))
            return list(user)
        return None


    def validate_email(self, email:str):
        exist_email = False
        user = self.get_user(email)
        if user:
            exist_email = True  
        return exist_email


    def update_user(self, new_username:str, email:str):
        db.update_user(new_username, email)
     
                
    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.password}')"
