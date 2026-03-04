import os
from openai import OpenAI

class ChatBot:
    """A chatbot that interacts with the OpenAI API to generate responses."""
    def __init__(self, api_key, model="gpt-4o-mini", temperature=0.7):
        self.api_key = api_key
        self.model = model
        self.temperature = temperature

    def generate_response(self, user_input):
        try:
            client = OpenAI(api_key=self.api_key)

            response = client.responses.create(
                model=self.model,
                input=user_input,
                temperature=self.temperature
            )

            return response.output_text

        except Exception as e:
            return f'An error occurred: {e}'


api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("OPENAI_API_KEY not set")

bot = ChatBot(api_key=api_key)
ai_respone = bot.generate_response("What are some groundbreaking AI advancements?'")
print(ai_respone)

python_respone = bot.generate_response("Explain about the python as 5 years kid")
print(python_respone)
