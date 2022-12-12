from crm_app import app
from crm_app import db
import requests
import configparser

if __name__ =='__main__':
    # with app.app_context():
    #     db.create_all()
    app.run(host='165.227.198.32', port=5000)