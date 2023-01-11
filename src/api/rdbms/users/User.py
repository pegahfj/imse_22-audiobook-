from flask_login import UserMixin

from src import db



class User:
    def __init__(self, id, usr, email, psw):
        self.id: int = id
        self.username: str = usr
        self.email: str = email
        self.password: str = psw
        self.collection = UserCollection(self.id)

    @classmethod
    def get_instance(cls, user:list):
        return User(user[0], user[1], user[2], user[3])

   
    def validate_email(email:str):
        exist_email = False
        user = db.get_user_byEmail(email)
        if user:
            exist_email = True  
        return exist_email

         
    def get(user_id:int):
        user = db.get_user_byEmail(user_id)
        if user:
            return User.get_instance(user)
        return None

      
    def get_byEmail(email:str):
        user = db.get_user_byEmail(email)
        if user:
            return User.get_instance(user)
        return None

    
    def insert(user, email, passw):
            o = db.insert_single_user(user, email, passw)
            if type(o) is int:
                return o
            else:
                return None


    # def update_user(self, new_username:str, email:str):
    #     db.update_user(new_username, email)
     
                
    # def __repr__(self):
    #     return f"User('{self.username}', '{self.email}', '{self.password}')"



class UserCollection:
    books:list 
    def __init__(self, id):
        user_id = id
        
    @classmethod     
    def get(cls, user_id:int):
        user = db.get_user_byEmail(user_id)
        if user:
            return User.get_instance(user)
        return None

    @classmethod  
    def get_byEmail(cls, email:str):
        user = db.get_user_byEmail(email)
        if user:
            return User.get_instance(user)
        return None

    @classmethod
    def insert(cls, user='test', email='test', passw='test'):
            o = db.insert_single_user(user, email, passw)
            if type(o) is int:
                return o
            else:
                return None