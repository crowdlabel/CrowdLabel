from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from .basicbase import Base


MAX_EMAIL_LENGTH = 320 # RFC
VERIFICATION_CODE_LENGTH = 6

class Email(Base):
    __tablename__ = 'email'
    email = Column(String(MAX_EMAIL_LENGTH),unique = True ,primary_key = True)
    verification_code = Column(String(VERIFICATION_CODE_LENGTH))

    def __init__(self, email, code):
        self.email = email
        self.verification_code = code