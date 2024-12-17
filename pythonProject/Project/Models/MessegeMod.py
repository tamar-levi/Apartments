from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from ..app import db

class Messege(db.Model):
    __tablename__ = 'messages'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_mail = Column(Integer, ForeignKey('users.id'))
    content = Column(String(255), nullable=False)

    user = relationship("User", back_populates="messages")
