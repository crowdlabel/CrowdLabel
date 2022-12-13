from pydantic import BaseModel
from datetime import datetime

class AnswerType(BaseModel):
    pass

class SingleChoiceAnswer(AnswerType):
    choice: int

class MultiChoiceAnswer(AnswerType):
    choices: list[int]

class RankingAnswer(AnswerType):
    ranking: list[int]

class OpenAnswer(AnswerType):
    text: str

class Point(BaseModel):
    x: int
    y: int

class BoundingBoxAnswer(AnswerType):
    top_left: Point
    bottom_right: Point

class Answer(BaseModel):
    respondent: str # username of respondent
    date_answered: datetime
    task_id: int
    question_id: int
    question_type: int
    answer: AnswerType | None