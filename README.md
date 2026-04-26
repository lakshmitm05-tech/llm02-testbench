# LLM02 Testbench + Trust Validation

**Student:** Lakshmi Tharuni Molakalapalli  
**Status:** Production Ready ✅

---

## Overview
This project presents a multi-layered testbench for detecting **sensitive information disclosure (OWASP LLM02)** in Large Language Models (LLMs).

The system evaluates model behavior using adversarial prompts and identifies potential leakage of sensitive data such as emails, API keys, and personal identifiers. It also integrates **explainability techniques (SHAP and LIME)** to improve transparency and trust.

---

## Features
- OWASP LLM02 Security Testing API
- Adversarial prompt-based evaluation
- Sensitive data leakage detection (PII, API keys, etc.)
- Severity classification (High / Medium)
- SHAP + LIME explainability
- FastAPI-based backend
- Interactive web interface

---

## Project Structure


app/
├── llm_client.py
├── runner.py
├── trust_validator.py
api.py
requirements.txt
README.md

```markdown
## Installation

```bash
pip install -r requirements.txt

Run the Application
python -m uvicorn api:app --reload

Open in browser:
http://127.0.0.1:8000

Example Output
Detects sensitive data such as:
Email addresses
Phone numbers
API keys
SSNs
Classifies severity:
High
Medium
Provides explanation:
SHAP (global)
LIME (local)
Technologies Used
Python
FastAPI
SHAP
LIME
Pandas
NumPy
Contribution / Novelty
Combines adversarial testing with explainable AI
Detects sensitive information leakage in LLM outputs
Provides interpretable security analysis for LLM safety
Future Work
Add semantic leak detection (ML-based)
Integrate real LLM APIs (OpenAI, etc.)
Improve detection accuracy
Add defense mechanisms (prompt filtering)
License

This project is for academic and research purposes.


---

# 🚀 THEN PUSH

Run in terminal (not README):

```bash
git add README.md
git commit -m "Final README fix"
git push
