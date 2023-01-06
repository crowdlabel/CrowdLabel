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
                new_answer = schemas.answers.MultiChoiceAnswer(choices = [] if ans.choices == '' else [int(choice) for choice in ans.choices.split('|')])
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
                res = await con.execute(select(models.answer.BoundingBoxAnswer).where(models.answer.BoundingBoxAnswer.id == answer.id).options(selectinload(models.answer.BoundingBoxAnswer.corner)))
                ans = res.scalars().first()
                boxes = []
                for corner in ans.corner:
                    p1 = schemas.answers.Point(x = corner.top_left_x, y =corner.top_left_y)
                    p2 = schemas.answers.Point(x = corner.bottom_right_x, y =corner.bottom_right_y)
                    new_corner = schemas.answers.Corners(top_left=p1,bottom_right = p2)
                    boxes.append(new_corner)
                new_answer = schemas.answers.BoundingBoxAnswer(boxes = boxes)
                new_question.answers.append(new_answer)
        elif  type == 'open':
            new_question = schemas.questions.OpenQuestion(**di)
            for answer in target.answer:
                res = await con.execute(select(models.answer.OpenAnswer).where(models.answer.OpenAnswer.id == answer.id))
                ans = res.scalars().first()
                new_answer = schemas.answers.OpenAnswer(text = ans.text)
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
        print(target.answer)
        if target_answer == None:
            if isinstance(answer,schemas.answers.MultiChoiceAnswer):
                if target.question_type != 'multi_choice':
                    await asyncio.shield(con.close())
                    return f'type mismatch , question type {target.question_type} ,answer type multi_choice'
                new_answer = models.answer.MultiChoiceAnswer()
                new_answer.choices = '|'.join([str(choice) for choice in answer.choices])
            elif isinstance(answer,schemas.answers.SingleChoiceAnswer):
                if target.question_type != 'single_choice':
                    await asyncio.shield(con.close())
                    return f'type mismatch , question type {target.question_type} ,answer type single_choice'
                new_answer = models.answer.SingleChoiceAnswer()
                new_answer.choice = answer.choice
            elif  isinstance(answer,schemas.answers.BoundingBoxAnswer):
                if target.question_type != 'bounding_box':
                    await asyncio.shield(con.close())
                    return f'type mismatch , question type {target.question_type} ,answer type bounding_box'
                new_answer = models.answer.BoundingBoxAnswer()
                for corner in answer.boxes:
                    new_corner = models.answer.Corner()
                    new_corner.top_left_x = corner.top_left.x
                    new_corner.top_left_y = corner.top_left.y
                    new_corner.bottom_right_x = corner.bottom_right.x
                    new_corner.bottom_right_y = corner.bottom_right.y
                    new_corner.answer_id = target.id
                    con.add(new_corner)
                    new_answer.corner.append(new_corner)
            elif  isinstance(answer,schemas.answers.OpenAnswer):
                if target.question_type != 'open':
                    await asyncio.shield(con.close())
                    return f'type mismatch , question type {target.question_type} ,answer type open'
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
                print(answer)
                print(2)
                target.choices = '|'.join([str(choice) for choice in answer.choices])
            elif isinstance(answer,schemas.answers.SingleChoiceAnswer):
                res = await con.execute(select(models.answer.SingleChoiceAnswer).where(and_(models.answer.SingleChoiceAnswer.respondent_name == respondent.username,models.answer.SingleChoiceAnswer.question_id == target.id)))
                target = res.scalars().first()
                target.choice = answer.choice
            elif  isinstance(answer,schemas.answers.BoundingBoxAnswer):
                res = await con.execute(select(models.answer.BoundingBoxAnswer).where(and_(models.answer.BoundingBoxAnswer.respondent_name == respondent.username,models.answer.BoundingBoxAnswer.question_id == target.id)).options(selectinload(models.answer.BoundingBoxAnswer.corner)).options(selectinload(models.answer.BoundingBoxAnswer.corner)))
                target = res.scalars().first()
                target.corner = []
                for corner in answer.boxes:
                    new_corner = models.answer.Corner()
                    new_corner.top_left_x = corner.top_left.x
                    new_corner.top_left_y = corner.top_left.y
                    new_corner.bottom_right_x = corner.bottom_right.x
                    new_corner.bottom_right_y = corner.bottom_right.y
                    new_corner.answer_id = target.id
                    con.add(new_corner)
                    target.corner.append(new_corner)
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