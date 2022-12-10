from fastapi import Depends, Path
from fastapi.routing import APIRouter
from schemas.questions import Answer
from .auth import get_current_user
import services.questions as qs


router = APIRouter()



@router.post('')
async def create_answer(answer: Answer, task_id: int=Path(), question_id: int=Path(), current_user=Depends(get_current_user)):
    return qs.answer(current_user, task_id, question_id, answer)
