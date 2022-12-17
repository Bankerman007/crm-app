from crm_app import db, login_manager
from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id= db.Column(db.Integer, primary_key=True)
    username= db.Column(db.String(20), unique= True, nullable=False)
    email= db.Column(db.String(120), unique= True, nullable=False)
    image_file= db.Column(db.String(20), nullable=False, default= 'default.jpeg')
    password= db.Column(db.String(60), nullable=False)
    contacts= db.relationship('Contacts', backref='username', lazy=True)

    def __repr__(self):
        return f"User('{self.id},'{self.username}','{self.email}','{self.image_file},'{self.contacts}')"

class Contacts(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String(100),nullable=False)
    phone= db.Column(db.Integer, nullable=True)
    email= db.Column(db.String(120), unique= True, nullable=False)
    notes= db.Column(db.Text, nullable=True)
    user_id= db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Contacts('{self.name}','{self.phone}','{self.user_id})"

# with app.app_context():
#     contact_1=Contacts(id='1', name='Thor', phone='8475555555',email='thor@thor.com',notes='strongest avenger',user_id='1')
#     db.session.add(contact_1)
#     db.session.commit()
#     print(Contacts.query.all())