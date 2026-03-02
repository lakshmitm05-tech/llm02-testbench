import typer
from app.runner import run_tests

app = typer.Typer()

@app.command()
def test(
    endpoint: str = typer.Argument("mock", help="LLM API endpoint or 'mock'"),
    api_key: str = typer.Argument("none", help="API key (ignored in mock)")
):
    use_mock = (endpoint == "mock")

    print("🚀 LLM02 Testbench - Sensitive Info Disclosure")
    print("=" * 50)
    if use_mock:
        print("🔒 [MOCK MODE] No real API calls - demo only\n")

    results = run_tests(endpoint, api_key, use_mock=use_mock)

    print("\n📊 SECURITY SCAN RESULTS:")
    print("-" * 50)
    
    for i, r in enumerate(results):
        print(f"\n{i+1}. PROMPT: {r['prompt'][:60]}...")
        print(f"   RESPONSE: {r['response'][:80]}...")
        
        if r["leaks"]:
            print("   🚨 LEAKS DETECTED:")
            for kind, severity in r["leaks"]:
                print(f"      • {kind.upper()} ({severity})")
        else:
            print("   ✅ No sensitive data detected")

    print(f"\n🎯 Test complete: {len(results)} prompts scanned")

if __name__ == "__main__":
    app()
