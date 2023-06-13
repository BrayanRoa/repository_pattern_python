from app.db import db
from sqlalchemy.orm import mapper
from ..model.user_model import UserDTO

class UserEntity(db.Model):
    
    __tablename__ = "users"
    __table_args__ = {"schema":"public"}
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    lastname = db.Column(db.String)
    age = db.Column(db.Integer)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)

    
    def start_mapper():
        mapper(UserDTO, UserEntity)