# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from flask_bcrypt import Bcrypt
# from flask_login import LoginManager
# from crm_app import app
# from crm_app import db
# from crm_app.models import Contacts, User
# from sqlalchemy import engine
# from sqlalchemy import select
# from sqlalchemy.orm import Session

# with app.app_context():
#     db.create_all()
    #app.run(debug=True)
    
    # app = Flask(__name__)
    # app.config['SECRET_KEY']= 'r46ttr29ara'
    # app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///site.db' 
    # db = SQLAlchemy(app)
    # bcrypt=Bcrypt(app)
    # login_manager= LoginManager(app)
    # login_manager.login_view= 'login'
    # login_manager.login_message_category= 'info'

    #with Session(engine) as session:
    #statement = select(Contacts).filter(Contacts.user_id == '2')
    #statement = session.query(Contacts).filter(Contacts.user_id == 1)
    #print(statement)
    
    # user= User.query.get(1)
    # user=user.contacts
    # print(user)

    #contacts = Contacts.query.all()
    #contacts = Contacts.query.filter(Contacts.user_id== 1)
    #contacts =  Contacts.query.get(Contacts.user_id==1)
        

    #print(contacts)




# def test():
#     contact=Contacts.query.get_or_404()
#     print(contact)




# with app.app_context():
#     db.create_all()
#     test()


#  <a class="btn btn-secondary btn-sm mt-1 mb-1" href="{{ url_for('update_contact', id=contact.id) }}">Update</a>
#           <form action="{{ url_for('delete_contact', id=contact.id)}}" method='POST'><input class="btn btn-danger btn-sm" type="submit" value="Delete">
