import requests
import os

url = "https://api.openai.com/v1/chat/completions"

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {os.environ['OPENAI_API_KEY']}"
}

data = {
    "model": "gpt-4o-mini",
    "temperature": 0.7,
    # "prompt": "explain python as 5 years kid"
    "messages": [
        {
            "role": "system", "content": "You are a helpful assistant."
        },
        {
            "role": "user", "content": "What are some groundbreaking AI advancements?"
        }
    ]
}
try:
    response = requests.post(url, headers=headers, json=data)
    print(response.status_code)
    if response.status_code == 200:
        result = response.json()

        # Extract assistant message
        assistant_reply = result["choices"][0]["message"]["content"]

        print("Assistant:", assistant_reply)
    else:
        print(f'Error: {response.status_code} - {response.text}')
except Exception as e:
    print(f'An error occurred: {e}')