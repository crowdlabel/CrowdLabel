from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


MAX_USERNAME_LENGTH = 64
CIPHER_LENGTH = 97 # len(hash('test'))
MAX_EMAIL_LENGTH = 320 # RFC

class User(Base):
    __tablename__ = 'user'
    username = Column(String(MAX_USERNAME_LENGTH), unique=True, primary_key=True)
    password_cipher = Column(String(CIPHER_LENGTH))
    email = Column(String(MAX_EMAIL_LENGTH))
    usertype = Column(Integer)
    status = Column(Integer)
    verification_code = Column(String(6))

    def __init__(self, username, password, email, usertype, status, verification_code='000000'):
        self.username = username
        self.password = password
        self.email = email
        self.usertype = usertype
        self.status = status
        self.verfication_code = verification_code
