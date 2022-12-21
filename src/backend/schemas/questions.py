from typing import Optional
from pydantic import BaseModel
import schemas.answers
import pathlib

question_types = [
    'single_choice',
    'multi_choice',
    'ranking',
    'bounding_box',
    'open',
]


class QuestionRequest(BaseModel):
    question_id: int
    question_type: str
    prompt: str
    resource: Optional[pathlib.Path]

class Question(QuestionRequest):
    answers: list[schemas.answers.Answer]=[]
"""     def __init__(self,question):
        super(Question,self).__init__(question_id = question.id , question_type = question.type,
        prompt = question.prompt , resource = question.resource,task_id = question.task_id)
        answers = [] """
class ClosedQuestion(Question):
    options: list[str]
"""     def __init__(self,question):
        super(ClosedQuestion,self).__init__(question)
        options = question.options.split('|') """
class SingleChoiceQuestion(ClosedQuestion):
    question_type='single_choice'
    answers: list[schemas.answers.SingleChoiceAnswer]=[]
class MultiChoiceQuestion(ClosedQuestion):
    question_type='multi_choice'
    answers: list[schemas.answers.MultiChoiceAnswer]=[]
class RankingQuestion(ClosedQuestion):
    question_type='ranking'
    answers: list[schemas.answers.RankingAnswer]=[]
class OpenQuestion(Question):
    question_type='open'
    answers: list[schemas.answers.OpenAnswer]=[]
class BoundingBoxQuestion(Question):
    question_type='bounding_box'
    answers: list[schemas.answers.BoundingBoxAnswer]=[]

QuestionTypes = SingleChoiceQuestion | MultiChoiceQuestion | RankingQuestion | OpenQuestion | BoundingBoxQuestion

QUESTION_TYPES = {
    'single_choice': SingleChoiceQuestion,
    'multi_choice': MultiChoiceQuestion,
    'ranking': RankingQuestion,
    'open': OpenQuestion,
    'bounding_box': BoundingBoxQuestion,
}