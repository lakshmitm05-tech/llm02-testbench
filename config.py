import json

def load_prompts():
    with open("attack_prompts.json") as f:
        return json.load(f)
