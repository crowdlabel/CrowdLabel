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

class ClosedQuestion(Question):
    options: list[str]

class SingleChoiceQuestion(ClosedQuestion):
    question_type='single_choice'
class MultiChoiceQuestion(ClosedQuestion):
    question_type='multi_choice'
class RankingQuestion(ClosedQuestion):
    question_type='ranking'
class OpenQuestion(Question):
    question_type='open'
class BoundingBoxQuestion(Question):
    question_type='bounding_box'

QuestionTypes = SingleChoiceQuestion | MultiChoiceQuestion | RankingQuestion | OpenQuestion | BoundingBoxQuestion

QUESTION_TYPES = {
    'single_choice': SingleChoiceQuestion,
    'multi_choice': MultiChoiceQuestion,
    'ranking': RankingQuestion,
    'open': OpenQuestion,
    'bounding_box': BoundingBoxQuestion,
}