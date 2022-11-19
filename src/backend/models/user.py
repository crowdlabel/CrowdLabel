from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from .basicbase import Base


MAX_USERNAME_LENGTH = 64
HASH_LENGTH = 97 # len(hash('test'))
MAX_EMAIL_LENGTH = 320 # RFC
VERIFICATION_CODE_LENGTH = 6

class User(Base):
    __tablename__ = 'user'
    username = Column(String(MAX_USERNAME_LENGTH), unique=True, primary_key=True)
    password_hashed = Column(String(HASH_LENGTH))
    email = Column(String(MAX_EMAIL_LENGTH))
    user_type = Column(Integer)
    status = Column(Integer)

    def __init__(self, username, password_hashed, email, user_type, status):
        self.username = username
        self.password_hashed = password_hashed
        self.email = email
        self.user_type = user_type
        self.status = status
