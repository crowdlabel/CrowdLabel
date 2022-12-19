from pydantic import BaseModel
import schemas.answers


question_types = [
    'single_choice',
    'multi_choice',
    'ranking',
    'bounding_box',
    'open',
]


class Question(BaseModel):
    question_id: int
    question_type: str
    prompt: str
    resource: str | None
    task_id: int
    answers: list[schemas.answers.Answer]
    def __init__(self,question):
        super(Question,self).__init__(question_id = question.id , question_type = question.type,
        prompt = question.prompt , resource = question.resource,task_id = question.task_id)
        answers = []
class ClosedQuestion(Question):
    options: list[str]
    def __init__(self,question):
        super(ClosedQuestion,self).__init__(question)
        options = question.options.split('|')
class SingleChoiceQuestion(ClosedQuestion):
    question_type='single_choice'
class MultiChoiceQuestion(ClosedQuestion):
    question_type='multi_choice'
class RankingQuestion(ClosedQuestion):
    question_type='ranking'
class OpenQuestion(Question):
    question_type='open'

   

class ClosedQuestion(Question):
    options: list[str]