class Question:
    """
    Questions are the units that make up a task.
    A question must have a prompt that is presented to the user.
    The user can then respond to the prompt using various methods.
    These methods are defined by the subclasses of `Question`.
    Questions may have a known answer, and the answer may be used
    to 
    """
    def __init__(self, prompt, answer) -> None:
        pass

class MultipleChoice(Question):
    def __init__(self, type, prompt, options, answer=None) -> None:
        super().__init__(type, prompt, answer)

class Ranking(Question):
    def __init__(self) -> None:
        super().__init__()
