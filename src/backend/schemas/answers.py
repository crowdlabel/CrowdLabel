from pydantic import BaseModel
from datetime import datetime

class Answer(BaseModel):
    respondent: str # username of respondent
    date_answered: datetime
    task_id: int
    question_id: int
    question_type: int
    answer: str

class SingleChoiceAnswer(Answer):
    answer: int

class MultiChoiceAnswer(Answer):
    answer: list[int]

class RankingAnswer(Answer):
    answer: list[int]

class OpenAnswer(Answer):
    answer: str

class Point(BaseModel):
    x: int
    y: int

class BoundingBoxAnswer(Answer):
    answer: list[Point, Point]

