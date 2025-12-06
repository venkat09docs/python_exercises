# PARSING JSON DATA FROM API RESPONSES

import json
import requests

# Define the API URL
url = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(url)

# Status Codes
# 2xx Successful responses
# 3xx Redirection messages
# 4xx Client error responses
# 5xx Server error responses

posts_data = json.loads(response.text)
print(type(posts_data))

# for item in posts_data:
#     print(item['title'])

print(posts_data[40]['title'])

# Example of a JSON response containing API usage details and choices
response = {
    "usage": {
        "total_tokens": 1000,
        "details": {"prompt_tokens": 300, "completion_tokens": 700}
    },
    "choices": [
        {"text": "The capital of France is Paris.", "index": 0},
        {"text": "France's capital is Paris.", "index": 1}
    ]
}

print(response['usage']['total_tokens'])
# print(response['choices']['text'])
# for item in response['choices']:
#     print(item['text'])

choice_texts = [item['text'] for item in response['choices']]
print(choice_texts)