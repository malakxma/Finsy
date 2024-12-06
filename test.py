import anthropic

client = anthropic.Anthropic(api_key="Insert API key here")

try:
    response = client.messages.create(
        model="claude-3-5-sonnet-20241022",
        max_tokens=1024,
        messages=[
            {"role": "user", "content": "Hello, Claude!"}
        ]
    )
    print(response)
except Exception as e:
    print(f"Error: {e}")

