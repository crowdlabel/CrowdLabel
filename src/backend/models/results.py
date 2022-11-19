from sqlalchemy import Column, Integer, String ,DateTime
from sqlalchemy.ext.declarative import declarative_base
from .basicbase import Base


MAX_USERNAME_LENGTH = 64
HASH_LENGTH = 97 # len(hash('test'))
MAX_EMAIL_LENGTH = 320 # RFC
VERIFICATION_CODE_LENGTH = 6

class Results(Base):
    __tablename__ = 'result'
    id = Column(Integer,unique=True,primary_key = True)
    name = Column(String(MAX_USERNAME_LENGTH))
    date_created = Column(DateTime)
    date_download = Column(DateTime)
    def __init__(self, id, name,date_created,date_download):
        self.id = id 
        self.name = name 
        self.date_created = date_created
        self.date_download = date_download