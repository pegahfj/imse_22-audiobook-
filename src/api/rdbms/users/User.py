from flask_login import UserMixin

from src import db, login_manager


# @login_manager.user_loader
# def load_user(user_id:int):
#     return User.get(int(user_id))

class User():
    def __init__(self, user='test', email='test', passw='test'):
        self.id: int 
        self.username: str = user
        self.email: str = email
        self.password: str = passw


    def insert(self):
        o = db.insert_single_user(self.username, self.email, self.password)
        if type(o) is int:
            self.id = o
            return self.id 
        else:
            return None
    
      
    def get(self, user_id:int):
        user = db.get_user_byEmail(user_id)
        if user:
            return User(user[1], user[2], user[3])
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





    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True

    def get_id(self):
        return str(self.id)


# class Post(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(100), nullable=False)
#     date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
#     content = db.Column(db.Text, nullable=False)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

#     def __repr__(self):
#         return f"Post('{self.title}', '{self.date_posted}')"
