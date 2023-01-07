# from flask_login import UserMixin

from src import db

class User():
    def __init__(self):
        self.id: int 
        self.username: str 
        self.email: str
        self.password: str 

    def insert_user(self, username:str, email:str, password:str):
        o = db.insert_user(username, email, password)

        if type(o) is int:
            self.id = o
            self.username= username
            self.email = email
            self.password = password
            return True

        else:
            return False
      
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

    def update_user(self, new_username:str, email:str):
        val = (new_username, email)
        self.cursor.execute(User.update, val)
        self.connection.commit()
            
    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.password}')"
