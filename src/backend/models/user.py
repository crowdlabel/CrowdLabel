from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


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
    verification_code = Column(String(VERIFICATION_CODE_LENGTH))

    def __init__(self, username, password, email, user_type, status, verification_code='000000'):
        self.username = username
        self.password = password
        self.email = email
        self.user_type = user_type
        self.status = status
        self.verfication_code = verification_code
