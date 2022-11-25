# Task format

```
{
    "name": "str, name of the task",
    "questions": [
        {
            "id": "int, ID of the question, must be unique to the current task",
            "type": "ranking | multichoice | singlechoice | ...",
            "prompt": "str",
            "resource": "str (relative filename) (optional)",
            "options": [
                "list of options for question types that require it"
            ]
        },
        ...
    ]
}
```

This JSON file is to be saved as `task.json`. The file extensions of all other resources should match the content in order for the resource to be rendered properly.