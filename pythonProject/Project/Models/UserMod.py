from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from pythonProject.Project.db import db
class User(db.Model):
    __tablename__ = 'USERS'

    firstName = db.Column(db.String(50), nullable=False)
    lastName = db.Column(db.String(50), nullable=False)
    mail = db.Column(db.String(100), unique=True, nullable=False,primary_key=True)
    phon = db.Column(db.String(10), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    passwordResetToken = db.Column(db.String(100), nullable=True)  # Adding password reset token field
    # messages = relationship("Messege", back_populates="user")


