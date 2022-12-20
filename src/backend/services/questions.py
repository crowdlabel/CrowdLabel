import json


from sqlalchemy.orm import sessionmaker, scoped_session,selectinload
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select ,update,and_
from .database import *
Connection = sessionmaker(bind=engine,expire_on_commit=False,class_=AsyncSession)
con = scoped_session(Connection)
def __verify_question_format():
    return True


import models.question
import models.task
import models.user

import schemas.answers
import schemas.questions
import schemas.tasks
import schemas.users

import services.tasks


class Questions:
    async def get_question(self, task: schemas.tasks.Task | int, question_id: int) -> schemas.questions.Question | None:
        id = task.task_id
        result = await con.execute(select(models.question.Question).where(and_( models.question.Question.task_id == id , models.question.Question.id_in_task == question_id))
                                  .options(selectinload(models.question.Question.answer)))
        target = result.scalars().first()
        if target == None:
            return None
        type = target.question_type
        prompt = target.prompt
        resource = target.resource
        di = target.dict()
        del di['id_in_task']
        del di['options']
        di['question_id'] = target.id_in_task
        di['answers'] = []
        options = target.options.split('|')
        if type == 'multi_choice':
            di['options'] = target.options.split('|')
            new_answer = schemas.questions.MultiChoiceQuestion(**di)
        elif  type == 'single_choice':
            di['options'] = target.options.split('|')
            new_answer = schemas.questions.SingleChoiceQuestion(**di)
        elif  type == 'bounding_box':
            new_answer = schemas.questions.BoundingBoxQuestion(**di)
        elif  type == 'open':
            new_answer = schemas.questions.OpenQuestion(**di
                                                          )
        return new_answer
    async def create_answer(self, 
        current_user: schemas.users.User,
        answer: schemas.answers.AnswerRequest,
    ) -> str | None:

        # TODO
        if answer.question_type == 'multi_choice':
            new_answer = schemas.answers.MultiChoiceAnswer()
        elif  answer.question_type == 'single_choice':
            new_answer = schemas.answers.SingleChoiceAnswer()
        elif  answer.question_type == 'bounding_box':
            new_answer = schemas.answers.BoundingBoxAnswer()
        elif  answer.question_type == 'open':
            new_answer = schemas.answers.OpenAnswer()

        
        new_answer.date_answered = answer.date_answered
        new_answer.question_id = self.question_id
        res= await con.execute(select(models.user.Respondent).where(models.user.Respondent.username == answer.respondent))
        target = res.scalar().first
        new_answer.respondent_id = target.id
        new_answer.question_type = answer.question_type
        new_answer.respondent_name = answer.respondent
        return True
        
    async def create_question(self,id_in_task,type,prompt,file_path,options,task_id) ->models.question.Question:
        # if not __verify_question_format():
        #     return None
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
        file = json.load(open(file_path,'r'))
        response_questions = []
        result = await con.execute(select(models.task.Task).where(models.task.Task.id==task_id))
        target = result.scalars().first()
        if target == None:
            return None
        type = target.type
        try:
            for question in file:
                question = await self.create_question(file[question]['type'],file[question]['prompt'],file[question]['file_path'],file[question]['options'],task_id)
                response_questions.append(question)
        except:
            return None
        return response_questions

    # async def get_question(self, task_id: int, question_id: int) -> schemas.questions.Question | None:

    #     async with con.begin():
    #         result = await con.execute(select(models.question.Question).where(models.question.Question.id==id))
    #         target = result.scalars().first()
    #         if target is None:
    #             return{
    #                 "status":"not found",
    #             },400
    #     return {
    #         "status":"ok",
    #         "type" :target.type,
    #         "prompt":target.prompt,
    #         "resource":target.resource,
    #         "options":target.options,
    #         "task_id":target.task_id
    #     },200



    # async def edit_question(id,type,prompt,resource,options,task_id):
    #     async with con.begin():
    #         result = await con.execute(select(models.question.Question).where(models.question.Question.id==id))
    #         target = result.scalars().first()
    #         if target is None:
    #             return{
    #                 "status":"not found",
    #             },400
    #         target.type= type
    #         target.prompt =prompt
    #         target.resource = resource
    #         target.options = options
    #         target.task_id = task_id
    #         await con.flush()
    #         con.expunge(target)
    #     return {
    #         "status":"ok",
    #         "type" :target.type,
    #         "prompt":target.prompt,
    #         "resource":target.resource,
    #         "options":target.options,
    #         "task_id":target.task_id
    #     },200
        

    # async def delete_question(task_id, question_id):
    #     async with con.begin():
    #         result = await con.execute(select(models.question.Question).where(models.question.Question.id==id))
    #         target = result.scalars().first()
    #         if target == None:
    #             return {
    #                 "status": 'not found'
    #             },400
    #         await con.delete(target)
    #         # for item in result:
    #         #     await con.delete(item)
    #     await con.commit()
    #     return {
    #         'status':'ok'
    #     },200


question_service = Questions()