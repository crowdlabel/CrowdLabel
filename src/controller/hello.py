from .base import *


class HelloRequest(BaseModel):
    msg: str

class HelloResponse(BaseModel):
    hello: str

@app.post('/hello', response_model=HelloResponse)
async def hello(request: HelloRequest):
    return HelloResponse(hello=request.msg)