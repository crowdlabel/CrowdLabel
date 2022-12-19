from typing import Optional
from pydantic import BaseModel
import schemas.answers

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
    resource: Optional[str]

class Question(QuestionRequest):
    answers: list[schemas.answers.Answer]=[]

class ClosedQuestion(Question):
    options: list[str]

class SingleChoiceQuestion(ClosedQuestion):
    question_type='single_choice'
    answers: list[schemas.answers.SingleChoiceAnswer]
class MultiChoiceQuestion(ClosedQuestion):
    question_type='multi_choice'
    answers: list[schemas.answers.MultiChoiceAnswer]
class RankingQuestion(ClosedQuestion):
    question_type='ranking'
    answers: list[schemas.answers.RankingAnswer]
class OpenQuestion(Question):
    question_type='open'
    answers: list[schemas.answers.OpenAnswer]
class BoundingBoxQuestion(Question):
    question_type='bounding_box'
    answers: list[schemas.answers.BoundingBoxAnswer]


QUESTION_TYPES = {
    'single_choice': SingleChoiceQuestion,
    'multi_choice': MultiChoiceQuestion,
    'ranking': RankingQuestion,
    'open': OpenQuestion,
    'bounding_box': BoundingBoxQuestion,
}