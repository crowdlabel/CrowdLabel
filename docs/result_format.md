{
    "name": "str, name of the task",
    "id": "int: ID of the task",
    "date-created": "datetime when the task was uploaded",
    "date-downloaded": "datetime when these results were downloaded",
    "results": [
        {
            "id": "int, ID of the question",
            "responses": {
                "0": "int; id of the respondant. Consistent within the same task, i.e. User 1 who answered the Question 1 of Task 1 is the same as User 1 who answered Question 2 of Task 2, but not necessarily the same as User 2 who answered Question 1 of Task 2. Does not correspond to the respondant's username to maintain anonymity",
                "1": "...",
            }
        },
        ...
    ]
}