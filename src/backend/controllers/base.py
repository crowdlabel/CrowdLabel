from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware


origins = [
    'http://localhost:8082'
]

app = FastAPI(
    title='CrowdLabelAPI',
    description='API for CrowdLabel',
    version='0.1.0',
    
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)