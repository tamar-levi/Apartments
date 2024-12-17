from flask import  Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base
from flask_mail import Mail
from pythonProject.Project.db import db
app = Flask(__name__)
print('app')
from flask_sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI']='mssql+pyodbc://@localhost\\SQLEXPRESS01/USERS?driver=ODBC Driver 17 for SQL Server'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['MAIL_SERVER'] = 'smtp.gmail.com'  # כתובת שרת המייל
app.config['MAIL_PORT'] =587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = '0504108916SH@gmail.com'  # כתובת מייל רשומה בשרת המייל
app.config['MAIL_PASSWORD'] = 'SHANIFISHER'  # סיסמת המייל
app.config['SECRET_KEY'] = 'your_secret_key_here'

print('kkkk')
db.init_app(app)
with app.app_context():
    db.create_all()
    print('with')
print('db')
# print(db)


#db=SQLAlchemy(app)
#db.init_app(app)
#engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
#Base = declarative_base()
#Base.metadata.create_all(engine)
email = Mail(app)
print('mail')

#Session = sessionmaker(bind=engine)
#session = Session()


# from Routes.ApartmentRoutes import ApartmentRout
from Routes.UserRoutes import UserRout
# from Routes.MessegeRoutes import MessegeRout
# with app.app_context():
#     db.create_all()

# app.register_blueprint(ApartmentRout, url_prefix='/apartments')


app.register_blueprint(UserRout, url_prefix='/users')


# app.register_blueprint(MessegeRout, url_prefix='/messages')
if __name__ == '__main__':

    app.run(debug=True)





