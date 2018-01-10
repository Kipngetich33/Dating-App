from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
class User(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
    pass_secure = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True,index = True) 
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    is_available = db.Column(db.Boolean, unique=False, default=True) 
    age= db.Column(db.Integer) 
    status = db.Column(db.String(255))
    patner = db.Column(db.String(255))
    intrested_in = db.Column(db.String(255))
    
    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)

    @classmethod
    def get_match(cls,age): 
        matches1 = User.query.filter(User.age > age-5).all()
        matches2 = User.query.filter(User.age <age+5).all()
        match3 = set(matches1+matches2)
        match_list=[]
        match_list2=[]
        for match in match3:
            if match.is_available==True and match.intrested_in== 'Women' and match.status == 'Single':
                match_list2.append(match)
        

        return match_list2 

    def tear_down(self):
        User.match_list= []
        User.match_list2 = []




    def __repr__(self):
        return f'User {self.username}'
    

    

class Role(db.Model):
    __tablename__='roles'
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    users = db.relationship('User',backref = 'role',lazy="dynamic")

    def __repr__(self):
        return f'User {self.name}'