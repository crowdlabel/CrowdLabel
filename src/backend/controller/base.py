from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI(
    title='CrowdLabelAPI',
    description='API for CrowdLabel',
    version='0.1.0',
    
)