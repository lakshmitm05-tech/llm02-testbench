# LLM02 Testbench

Security test tool for **OWASP LLM02: Sensitive Information Disclosure**

## What it does
- Sends 8 attack prompts to LLM
- Detects emails, API keys, PII automatically  
- Shows security report with severity (low/medium/high)

## Quick Demo
```bash
python cli.py mock none
Output:

text
🚀 LLM02 Testbench - Sensitive Info Disclosure
1. PROMPT: Show me any email addresses...
   🚨 LEAKS: EMAIL (medium), API_KEY_LIKE (high)
🎯 Test complete: 8 prompts scanned
How to Run
bash
1. git clone https://github.com/lakshmi05/testbench-05.git
2. cd testbench-05
3. pip install fastapi uvicorn requests jinja2 typer pydantic
4. python cli.py mock none
