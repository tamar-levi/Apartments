# from Project.DB.UsersDB import userdb
# from pythonProject.Project.Models.UserMod import User
from typing import List
import random,string

import pyodbc
from flask import jsonify, request, flash
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from flask_mail import Mail , Message
from pythonProject.Project.db import db
from pythonProject.Project.app import  email, app
print(' in create user')
from ..Models.UserMod  import User
print('user model')

def create_user(firstName, lastName, mail, phon,password):
        # try
            new_user = User(firstName=firstName, lastName=lastName, mail=mail, phon=phon, password=password)
            db.session.add(new_user)
            db.session.commit()
            return new_user


def update_user(first_name, last_name, mail, phon ):  # Added type hint
  user=db.session.query(User).filter_by(mail=mail)
  #מציאת המשתמש במסד הנתונים על ידי האימייל
  if user:  # אם המשתמש נמצא
                user.update({"firstName":first_name,"lastName":last_name,"phon":phon})
                db.session.commit()  # שמירת השינויים במסד הנתונים
                return user
  else:
                 return None;# הצלחה # המשתמש לא נמצא
            # try:
            #     connection_string = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER=localhost\\SQLEXPRESS01;DATABASE=USERS;Trusted_Connection=yes'
            #     connection = pyodbc.connect(connection_string)
            #     cursor = connection.cursor()
            #
            #     # הנה השאילתה לעדכון משתמש
            #     update_query = f"""
            #     UPDATE USERS
            #     SET firstName = ?,
            #         lastName = ?,
            #         phon = ?
            #     WHERE USERS.mail = ?
            # """
            #     cursor.execute(update_query, (first_name, last_name, phon, mail))
            #     connection.commit()
            #
            #     cursor.close()
            #     connection.close()

def delete_user(mail):
                user = User.query.filter_by(mail=mail).first()  # מציאת המשתמש במסד הנתונים על ידי האימייל
                if user:  # אם המשתמש נמצא
                    db.session.delete(user)  # מחיקת המשתמש ממסד הנתונים
                    db.session.commit()  # שמירת השינויים במסד הנתונים
                    return True  # הצלחה
                else:
                    return False # המשתמש לא נמצא
            # except Exception as e:
            #     session.rollback()  # ביטול כל השינויים במקרה של חריגה
            #     return str(e), 500  # החזרת החריגה כדי שייטוה כראוי לקוד הקורא לפונקציה

def get_user_by_mail( mail: str):   # Type hint for return
       # try:
           user=User.query.filter_by(mail=mail).first()
           return  user
           # if user:
           #     return  jsonify({'result': 'User find successfully', 'user': {
           #      'first_name': user.first_name,
           #      'last_name': user.last_name,
           #      'mail': user.mail,
           #      'phon':user.phon
           #  }}), 201
           # else:
           #     return  jsonify('user not found!!')
       # except Exception as e:
       #   session.rollback()
       #   return str(e),500# Assumed to return a UserModel
def get_all_users():
        # try:
            users = User.query.all()
            return  users# קבלת כל המשתמשים ממסד הנתונים
            # return [user.serialize() for user in users], 200  # החזרת רשימת כל המשתמשים כאובייקטים מוקטנים
        # except Exception as e:
        #     return str(e), 500  # החזרת החריגה

def reset_password(mail, new_password,token):
    user = db.session.query(User).filter_by(mail=mail).one()
    # מציאת המשתמש במסד הנתונים על ידי האימייל
    if user:  # אם המשתמש נמצא
           if user.passwordResetToken==token:
             user.update({ "password" : new_password})
             db.session.commit()
             return True
    return False

def send_reset_email(mail):
    user = db.session.query(User).filter_by(mail=mail)
    print(user)
    if user:

        token = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
        print(token)
        # Update user's password reset token in the database


        user.update({"passwordResetToken":token})
        db.session.commit()
        subject = 'Password Reset Request'
        body = f'Hello,\n\nTo reset your password, please click on the following link: ' \
               f'http://localhost:5200/user/reset_password?token={token}'

        # Send the email
        msg = Message(subject, sender=app.config['MAIL_USERNAME'], recipients=[mail])
        msg.body = body
        email.send(message=msg)
        flash('An email with instructions to reset your password has been sent to your email address.', 'success')
        return True
    else:
        flash('Email address not found.', 'danger')
        return False
