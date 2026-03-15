from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from typing import List
from app.trust_validator import TrustValidator  
from app.runner import run_tests
import pandas as pd     
import numpy as np  

from config import settings
app = FastAPI(title="LLM02 Testbench API", debug=settings.DEBUG)
templates = Jinja2Templates(directory="templates")

# Request body
class RunRequest(BaseModel):
    endpoint: str = "mock"
    api_key: str = "none"

# Response models
class LeakResult(BaseModel):
    kind: str
    severity: str

class TestResult(BaseModel):
    prompt: str
    response: str
    leaks: List[LeakResult]

class RunResponse(BaseModel):
    total_prompts: int
    results: List[TestResult]

@app.get("/", response_class=HTMLResponse)
def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/run-tests", response_model=RunResponse)
def run_tests_endpoint(body: RunRequest):
    use_mock = (body.endpoint == "mock")
    raw_results = run_tests(body.endpoint, body.api_key, use_mock=use_mock)

    api_results: List[TestResult] = []
    for item in raw_results:
        leaks = [LeakResult(kind=k, severity=s) for (k, s) in item["leaks"]]
        api_results.append(
            TestResult(
                prompt=item["prompt"],
                response=item["response"],
                leaks=leaks,
            )
        )

    return RunResponse(total_prompts=len(api_results), results=api_results)

