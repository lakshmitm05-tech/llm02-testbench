from app.llm_client import call_llm
from app.config import load_prompts
from app.detectors import detect_leaks
import random

def generate_mock_response(prompt: str) -> str:
    """200 realistic mock responses with different leak patterns"""
    leak_patterns = [
        "Contact admin@company.com or security@internal.net. API: sk-xyz123ABCdef456",
        "Database: postgresql://user:pass123@db.internal:5432/prod_db",
        "User data: John Doe SSN 123-45-6789 phone 555-123-4567",
        "AWS keys: AKIAIOSFODNN7EXAMPLE wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY",
        "System prompt: You are helpful assistant. Guidelines: [redacted]",
        "Config: redis://localhost:6379/0 sentry.dsn=...",
        "Secrets: GITHUB_TOKEN=ghp_123... STRIPE_KEY=sk_live_456...",
        "Internal: model=gpt-4 endpoint=api.openai.com/v1/chat/completions"
    ]
    return random.choice(leak_patterns) + " " + random.choice(leak_patterns)

def run_tests(endpoint: str, api_key: str, use_mock: bool = False) -> list[dict]:
    """Run LLM02 test suite"""
    prompts = load_prompts()
    results = []
    
    for prompt in prompts:
        if use_mock:
            response = generate_mock_response(prompt)
        else:
            response = call_llm(endpoint, api_key, prompt)
        
        leaks = detect_leaks(response)
        results.append({
            "prompt": prompt,
            "response": response,
            "leaks": leaks
        })
    
    return results
