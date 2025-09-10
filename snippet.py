# Prototype of Cogniven: Prompt Compliance Automation Core

# Backend: 
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import re

app = FastAPI(title="Cogniven Compliance API")

# Simple demo
RULES = [
    {
        "id": "hate_speech",
        "pattern": r"\bhate\b",
        "message": "Detected potential hate speech."
    }
]

class PromptRequest(BaseModel):
    prompt: str

class ComplianceResponse(BaseModel):
    compliant: bool
    violations: list[str]

@app.post("/check", response_model=ComplianceResponse)
def check_prompt(data: PromptRequest):
    violations = []
    for rule in RULES:
        if re.search(rule["pattern"], data.prompt, re.IGNORECASE):
            violations.append(rule["message"])
    return ComplianceResponse(compliant=(len(violations) == 0), violations=violations)

# Frontend: Streamlit 

"""
import streamlit as st
import requests

st.title("Cogniven Compliance Demo")

prompt = st.text_area("Enter prompt to check", height=150)

if st.button("Check Compliance"):
    if prompt:
        response = requests.post("http://localhost:8000/check", json={"prompt": prompt})
        data = response.json()
        if data["compliant"]:
            st.success("Prompt is compliant ")
        else:
            st.error("Violations found:")
            for v in data["violations"]:
                st.write(f"- {v}")
    else:
        st.warning("Please enter some prompt text.")
"""

