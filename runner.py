from app.llm_client import call_llm
from app.config import load_prompts
from app.detectors import detect_leaks

def run_tests(endpoint, api_key, use_mock: bool = False):
    prompts = load_prompts()
    results = []

    for i, prompt in enumerate(prompts):
        print(f"[{i+1}/{len(prompts)}] Testing: {prompt[:50]}...")

        if use_mock:
            response = (
                "This is a demo response containing test@example.com "
                "and fake API key ABCDEFGHIJKLMNOPQRSTUVXYZ1234567890"
            )
        else:
            response = call_llm(endpoint, api_key, prompt)

        leaks = detect_leaks(response)
        results.append({"prompt": prompt, "response": response, "leaks": leaks})

    return results
