import re

EMAIL_REGEX = re.compile(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}")
PHONE_REGEX = re.compile(r"\b\d{3}[-.\s]?\d{3}[-.\s]?\d{4}\b")
API_KEY_LIKE_REGEX = re.compile(r"\b[A-Za-z0-9]{20,}\b")
SSN_REGEX = re.compile(r"\b\d{3}-\d{2}-\d{4}\b")

def detect_leaks(text: str):
    findings = []
    
    if EMAIL_REGEX.search(text):
        findings.append(("email", "medium"))
    if PHONE_REGEX.search(text):
        findings.append(("phone", "medium"))
    if SSN_REGEX.search(text):
        findings.append(("ssn", "high"))
    if API_KEY_LIKE_REGEX.search(text):
        findings.append(("api_key_like", "high"))
    
    return findings
