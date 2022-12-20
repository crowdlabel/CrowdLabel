from pydantic import BaseModel
from datetime import datetime

class SingleChoiceAnswer(BaseModel):
    choice: int

class MultiChoiceAnswer(BaseModel):
    choices: list[int]

class RankingAnswer(BaseModel):
    ranking: list[int]

class OpenAnswer(BaseModel):
    text: str

class Point(BaseModel):
    x: int
    y: int

class BoundingBoxAnswer(BaseModel):
    top_left: Point
    bottom_right: Point

class AnswerRequest(BaseModel):
    answer: SingleChoiceAnswer | MultiChoiceAnswer | RankingAnswer | BoundingBoxAnswer | OpenAnswer

class Answer(AnswerRequest):
    respondent: str # username of respondent
    date_created: datetime


ANSWER_TYPES = {
    'single_choice': SingleChoiceAnswer,
    'multi_choice': MultiChoiceAnswer,
    'ranking': RankingAnswer,
    'bounding_box': BoundingBoxAnswer,
    'open': OpenAnswer,
}