import pytest
import main
from services.database import init_models_sync
from test_utils import client

import pathlib

from test_tasks import *




if __name__ == '__main__':
    """
    test_availability()
    test_register()
    test_login()
    test_get_me()
    test_credits()
    test_upload()
    test_search()
    test_get_task()
    test_claim()
    test_get_task_question_resource() 
    test_answer()
    test_cover()
    """
    #test_answer_type()
    test_answer_visibility()
