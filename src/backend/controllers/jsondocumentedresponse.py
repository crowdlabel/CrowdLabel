from fastapi.responses import JSONResponse
from pydantic import BaseModel, parse_obj_as


class JSONDocumentedResponse:
    def __init__(self, status_code, description, model=None):
        self.status_code = status_code
        self.description = description
        self.model = model
    def documentation(self):
        return {
            'description': self.description,
        }
    def response(self, data: BaseModel | dict):
        print('returning response')
        return JSONResponse(
            content=data if not self.model else data.dict(exclude_none=True),
            status_code=self.status_code
        )

def create_documentation(responses: list[JSONDocumentedResponse]):
    documentation = {}
    documentation['status_code'] = responses[0].status_code
    documentation['response_description'] = responses[0].description
    """  if responses[0].model:
        documentation['response_model'] = responses[0].model """
    documentation['responses'] = {}
    for response in responses[1:]:
        doc = response.documentation()
        if response.model:
            doc['model'] = response.model
        documentation['responses'][response.status_code] = doc

    return documentation