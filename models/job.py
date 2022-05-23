
from extensions import db

class Job(db.Model):
    """DatabaseModel
    argument -- id, title, description, salary 
        The Job Model is the datamodel for the database and the front end 
    Return: the data property
    """
    __tablename__ = 'jobs'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.String(1000), nullable=False)
    salary = db.Column(db.Integer)
    is_published = db.Column(db.Boolean(), default=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    @property
    def data(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'salary': self.salary,
            'is_published': self.is_published
        }

    @classmethod
    def get_all_published(cls):
        return cls.query.filter_by(is_published=True).all()
        
    @classmethod
    def get_all(cls):
        return cls.query.all()

    @classmethod
    def get_by_id(cls, Id):
        return cls.query.filter_by(id=Id).first()

    @classmethod
    def get_by_user_id(cls, userId):
        return cls.query.filter_by(user_id=userId).all()

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()