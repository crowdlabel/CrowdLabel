import json


from sqlalchemy.orm import sessionmaker, scoped_session,selectinload
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select ,update,and_
from .database import *
import datetime
Connection = sessionmaker(bind=engine,expire_on_commit=False,class_=AsyncSession)
def __verify_question_format():
    return True


import models.question
import models.task
import models.user
import models.answer

import schemas.answers
import schemas.questions
import schemas.tasks
import schemas.users


from datetime import datetime

class Questions:
    async def get_question(self, task: schemas.tasks.Task, question_id: int) -> schemas.questions.Question | None:
        con = scoped_session(Connection)
        print(task)
        id = task.task_id
        result = await con.execute(select(models.question.Question).where(and_( models.question.Question.task_id == id , models.question.Question.id_in_task == question_id))
                                  .options(selectinload(models.question.Question.answer)))
        target = result.scalars().first()
        if target == None:
            await asyncio.shield(con.close())
            return None
        type = target.question_type
        di = target.dict()
        del di['id_in_task']
        del di['options']
        di['question_id'] = target.id_in_task
        di['answers'] = []
        options = target.options.split('|')
        if type == 'multi_choice':
            di['options'] = target.options.split('|')
            new_question= schemas.questions.MultiChoiceQuestion(**di)
            for answer in target.answer:
                res = await con.execute(select(models.answer.MultiChoiceAnswer).where(models.answer.MultiChoiceAnswer.id == answer.id))
                ans = res.scalars().first()
                new_answer = schemas.answers.MultiChoiceAnswer(choices = ans.choices.split('|'))
                new_question.answers.append(new_answer)
        elif  type == 'single_choice':
            di['options'] = target.options.split('|')
            new_question = schemas.questions.SingleChoiceQuestion(**di)
            for answer in target.answer:
                res = await con.execute(select(models.answer.SingleChoiceAnswer).where(models.answer.SingleChoiceAnswer.id == answer.id))
                ans = res.scalars().first()
                new_answer = schemas.answers.SingleChoiceAnswer(choice = ans.choice)
                new_question.answers.append(new_answer)
        elif  type == 'bounding_box':
            new_question = schemas.questions.BoundingBoxQuestion(**di)
            for answer in target.answer:
                res = await con.execute(select(models.answer.BoundingBoxAnswer).where(models.answer.BoundingBoxAnswer.id == answer.id))
                ans = res.scalars().first()
                p1 = schemas.answers.Point(x = ans.top_left_x, y =ans.top_left_y)
                p2 = schemas.answers.Point(x = ans.bottom_right_x, y =ans.bottom_right_y)
                new_answer = schemas.answers.BoundingBoxAnswer(top_left=p1,bottom_right = p2)
                new_question.answers.append(new_answer)
        elif  type == 'open':
            new_question = schemas.questions.OpenQuestion(**di)
            for answer in target.answer:
                res = await con.execute(select(models.answer.OpenAnswer).where(models.answer.OpenAnswer.id == answer.id))
                ans = res.scalars().first()
                new_answer = schemas.answers.OpenAnswer(ans.text)
                new_question.answers.append(new_answer)
        await asyncio.shield(con.close())
        return new_question
    async def create_answer(self, 
        task_id:int ,
        question_id : int,
        current_user: schemas.users.User,
        answer: schemas.answers.AnswerRequest
    ) -> str | None:
        con = scoped_session(Connection)
        result = await con.execute(select(models.question.Question).where(and_( models.question.Question.task_id == task_id , models.question.Question.id_in_task == question_id))
                                  .options(selectinload(models.question.Question.answer)))
        # TODO
        target = result.scalars().first()
        if target == None:
            await asyncio.shield(con.close())
            return 'question not found'
        res= await con.execute(select(models.user.Respondent).where(models.user.Respondent.username == current_user.username))
        respondent = res.scalars().first()
        if respondent == None:
            await asyncio.shield(con.close())
            return 'respondent not found'
        res = await con.execute(select(models.answer.Answer).where(and_(models.answer.Answer.respondent_name == respondent.username,models.answer.Answer.question_id == target.id)))
        target_answer = res.scalars().first()
        if target_answer == None:
            if isinstance(answer,schemas.answers.MultiChoiceAnswer):
                new_answer = models.answer.MultiChoiceAnswer()
                new_answer.choices = '|'.join(answer.choices)
            elif isinstance(answer,schemas.answers.SingleChoiceAnswer):
                new_answer = models.answer.SingleChoiceAnswer()
                new_answer.choice = answer.choice
            elif  isinstance(answer,schemas.answers.BoundingBoxAnswer):
                new_answer = models.answer.BoundingBoxAnswer()
                new_answer.top_left_x = answer.top_left.x
                new_answer.top_left_y = answer.top_left.y
                new_answer.bottom_right_x = answer.bottom_right.x
                new_answer.bottom_right_y = answer.bottom_right.y
            elif  isinstance(answer,schemas.answers.OpenAnswer):
                new_answer = models.answer.OpenAnswer()
                new_answer.text = answer.text
            new_answer.date_answered = datetime.utcnow()
            new_answer.question_id = target.id
            new_answer.task_id = task_id

            new_answer.respondent_id = respondent.id
            new_answer.respondent_name = respondent.username
            con.add(new_answer)
            await con.commit()
        else:
            if isinstance(answer,schemas.answers.MultiChoiceAnswer):
                res = await con.execute(select(models.answer.MultiChoiceAnswer).where(and_(models.answer.MultiChoiceAnswer.respondent_name == respondent.username,models.answer.MultiChoiceAnswer.question_id == target.id)))
                target = res.scalars().first()
                target.choices = '|'.join(answer.choices)
            elif isinstance(answer,schemas.answers.SingleChoiceAnswer):
                res = await con.execute(select(models.answer.SingleChoiceAnswer).where(and_(models.answer.SingleChoiceAnswer.respondent_name == respondent.username,models.answer.SingleChoiceAnswer.question_id == target.id)))
                target = res.scalars().first()
                target.choice = answer.choice
            elif  isinstance(answer,schemas.answers.BoundingBoxAnswer):
                res = await con.execute(select(models.answer.BoundingBoxAnswer).where(and_(models.answer.BoundingBoxAnswer.respondent_name == respondent.username,models.answer.BoundingBoxAnswer.question_id == target.id)))
                target = res.scalars().first()
                target.top_left_x = answer.top_left.x
                target.top_left_y = answer.top_left.y
                target.bottom_right_x = answer.bottom_right.x
                target.bottom_right_y = answer.bottom_right.y
            elif  isinstance(answer,schemas.answers.OpenAnswer):
                res = await con.execute(select(models.answer.OpenAnswer).where(and_(models.answer.OpenAnswer.respondent_name == respondent.username,models.answer.OpenAnswer.question_id == target.id)))
                target = res.scalars().first()
                target.text = answer.text
            target.date_answered = datetime.utcnow()
            await con.flush() 
            con.expunge(target)
            await con.commit()
        await asyncio.shield(con.close())
        return None
        
    async def create_question(self,id_in_task,type,prompt,file_path,options,task_id) ->models.question.Question:
        # if not __verify_question_format():
        #     return None
        con = scoped_session(Connection)
        async with con.begin():
            if type == 'multi_choice':
                question = models.question.MultipleChoice(id_in_task,type,prompt,file_path,'|'.join(options),task_id)
            elif type == 'single_choice':
                question = models.question.SingeChoiceQuestion(id_in_task,type,prompt,file_path,'|'.join(options),task_id)
            elif type == 'bounding_box':
                question = models.question.BoundingBoxQuestion(id_in_task,type,prompt,file_path,'|'.join(options),task_id)
            elif type == 'open':
                question = models.question.OpenQuestion(id_in_task,type,prompt,file_path,'|'.join(options),task_id)
            con.add(question)
            await con.commit()
            await asyncio.shield(con.close())
        return question
    async def create_question_from_file(
        self,
        task_id:int,
        file_path:str
    )->list[schemas.questions.Question]:
        # TODO
        #if not __verify_question_format():
        #    return False
        con = scoped_session(Connection)
        file = json.load(open(file_path,'r'))
        response_questions = []
        result = await con.execute(select(models.task.Task).where(models.task.Task.id==task_id))
        target = result.scalars().first()
        if target == None:
            await asyncio.shield(con.close())
            return None
        type = target.type
        try:
            for question in file:
                question = await self.create_question(file[question]['type'],file[question]['prompt'],file[question]['file_path'],file[question]['options'],task_id)
                response_questions.append(question)
        except:
            await asyncio.shield(con.close())
            return None
        await asyncio.shield(con.close())
        return response_questions


question_service = Questions()