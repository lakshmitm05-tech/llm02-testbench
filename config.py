import json
import os

def load_prompts() -> list[str]:
    """Load prompts from prompts.json with UTF-8 encoding"""
    prompts_file = os.path.join(os.path.dirname(__file__), "prompts.json")
    
    # Use UTF-8 encoding explicitly to fix the error
    with open(prompts_file, 'r', encoding='utf-8') as f:
        return json.load(f)
