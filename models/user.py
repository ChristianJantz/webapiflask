
from passlib.hash import pbkdf2_sha512
from extensions import db

class User(db.Model):
    """User Model contains the user information for the App
    Keyword arguments:
    argument -- description
    Return: return_description
    """
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    useremail = db.Column(db.String(200), nullable=False, unique=True)
    userpassword = db.Column(db.String(1000))
    is_aktiv = db.Column(db.Boolean(), default=True)
    jobs = db.relationship('Job', backref='User')


    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    
    @classmethod
    def hash_password(cls, userpassword):
        return pbkdf2_sha512.hash(userpassword)

    @classmethod
    def verify_password(cls, clean_pwd, hashed_pwd):
        return pbkdf2_sha512.verify(clean_pwd, hashed_pwd)

    @property
    def data(self):
        return {
            'id': self.id,
            'useremail': self.useremail,
            'userpassword': self.userpassword,
            'is_aktiv' : self.is_aktiv
        }

    @classmethod
    def get_by_useremail(cls, mail):
        return cls.query.filter_by(useremail=mail).first()
    
    @classmethod
    def get_all_users(cls):
        return cls.query.all()