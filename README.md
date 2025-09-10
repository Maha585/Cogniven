# Cogniven
PEC Techathon 3.0 - Prompt Compliance Automation 

Cogniven - Prompt Compliance Automation
Overview
Cogniven is an automated prompt compliance system designed to ensure AI-generated content adheres to responsible AI principles. 
It detects and flags unsafe, biased, or harmful prompts in real-time using a combination of configurable rule-based checks and advanced ML/NLP models.

Features
Real-time prompt compliance checking via REST API.
Configurable compliance rules to cover bias, hate speech, misinformation, privacy, violence, and more.
ML-enhanced toxicity detection using transformer-based models (Hugging Face ToxicBERT).
Scalable batch processing of prompts.
Interactive compliance dashboard built with Streamlit for monitoring and managing rules.
Authentication and security via token-based authorization.
Detailed violation reporting with suggestions for improvement.

Technology Stack
Backend: Python, FastAPI
ML/NLP: Hugging Face Transformers, PyTorch
Frontend: Streamlit
Deployment: Docker containers, Cloud-ready (AWS/Azure/GCP)

Authentication: HTTP Bearer token (API Key)
