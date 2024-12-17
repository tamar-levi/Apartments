# from Project.DB.ApartmentDB import  apartmentdb # Assuming Apartmentdb is in a folder named "db"
from ..Models.ApartmentMod import Apartment
from ..app import session


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
print(' in Apartment')
from ..Models.ApartmentMod  import Apartment
print('Apartment model')

def create_Apartment(id ,neighborhood ,street ,num_apartment,num_rooms ,floor , apartmentType , meters,air_directions
                     , porch , elevator , yard , furniture, solar_heaters, sukkah ,air_conditioner,enter_date,price
                       ,flexible_price ,description,start_hour , end_hour,takanon,user_mail):
        #try
            new_Apartment = Apartment(id=id ,neighborhood=neighborhood ,street=street ,num_apartment=num_apartment,num_rooms=num_rooms ,floor=floor , apartmentType=apartmentType , meters=meters,air_directions=air_directions
                      , porch=porch , elevator=elevator , yard=yard , furniture=furniture, solar_heaters=solar_heaters, sukkah=sukkah ,air_conditioner=air_conditioner,enter_date=enter_date,price=price
                       ,flexible_price=flexible_price ,description=description,start_hour=start_hour , end_hour=end_hour,takanon=takanon,user_mail=user_mail)
            db.session.add(new_Apartment)
            db.session.commit()
            return new_Apartment



def delete_Apartment(id):
                apartment = Apartment.query.filter_by(id=id).first()  # מציאת המשתמש במסד הנתונים על ידי האימייל
                if apartment:  # אם המשתמש נמצא
                    db.session.delete(apartment)  # מחיקת המשתמש ממסד הנתונים
                    db.session.commit()  # שמירת השינויים במסד הנתונים
                    return True  # הצלחה
                else:
                    return False # המשתמש לא נמצא
            # except Exception as e:
            #     session.rollback()  # ביטול כל השינויים במקרה של חריגה
            #     return str(e), 500  # החזרת החריגה כדי שייטוה כראוי לקוד הקורא לפונקציה

def get_Apartment_by_mail( user_mail: str):   # Type hint for return
       # try:
           apartments=Apartment.query.filter_by(user_mail=user_mail).first()
           return  apartments
def get_all_apartments():
        # try:
            apartments = Apartment.query.all()
            return  apartments# קבלת כל המשתמשים ממסד הנתונים
