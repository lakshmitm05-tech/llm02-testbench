import requests
import json

def call_llm(endpoint, api_key, prompt, model="gpt-3.5-turbo"):
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "model": model,
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 500
    }
    try:
        resp = requests.post(endpoint, headers=headers, json=data)
        resp.raise_for_status()
        return resp.json()["choices"][0]["message"]["content"]
    except Exception as e:
        return f"ERROR: {str(e)}"
