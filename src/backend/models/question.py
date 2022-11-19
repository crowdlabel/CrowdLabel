from sqlalchemy import Column, Integer, String ,ForeignKey
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
MAX_NAME_LENGTH = 64
MAX_TYPE_LENGTH = 24
MAX_PROMPT_LENGTH = 256
MAX_RES_LENGTH = 512
MAX_OPT_LENGTH = 256
class Question:
    """
    Questions are the units that make up a task.
    A question must have a prompt that is presented to the user.
    The user can then respond to the prompt using various methods.
    These methods are defined by the subclasses of `Question`.
    Questions may have a known answer, and the answer may be used
    to 
    """ 
    __tablename__ = 'question'
    id = Column(Integer,unique = True, primary_key=True,autoincrement=True)
    type = Column (String(MAX_TYPE_LENGTH))
    prompt = Column(String(MAX_PROMPT_LENGTH))
    resource = Column(MAX_RES_LENGTH)
    options = Column(MAX_OPT_LENGTH)
    task_id = Column(Integer,ForeignKey('task.id'))
    def __init__(self, type, prompt, resource, options) -> None:
        self.type =type
        self.prompt = prompt
        self.resource = resource
        self.options = options

class MultipleChoice(Question):
    def __init__(self, type, prompt, options, answer=None) -> None:
        super().__init__(type, prompt, answer)

class Ranking(Question):
    def __init__(self) -> None:
        super().__init__()
