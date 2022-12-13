from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .jsondocumentedresponse import JSONDocumentedResponse


origins = [
    "http://localhost",
    "http://localhost:8082",
    "*"
]

app = FastAPI(
    title='CrowdLabelAPI',
    description='API for CrowdLabel',
    version='0.1.0',
    
)
app = FastAPI()#default_response_class=JSONDocumentedResponse)


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)