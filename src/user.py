"""
There are two types of users:
    - Requester: creates tasks to be completed
    - Worker: completes tasks
"""

class User:
    def __init__(self,
            username,
            password,
            name,
            email,
            phone) -> None:
        pass

class Requester(User):
    def __init__(self) -> None:
        super().__init__()

class Contractor(User):
    def __init__(self) -> None:
        super().__init__()

def get_user_info(username):
    pass