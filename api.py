import anthropic
import os
from dotenv import load_dotenv

load_dotenv()

api = os.getenv("ANTHROPIC_API_KEY").strip()
client = anthropic.Anthropic(api_key=api)

email_type = input("What type of email do you want to write? ")
response = client.messages.create(
    model="claude-3-5-sonnet-20241022",
    max_tokens=100,
    messages=[
        {
            "role": "assistant",
            "content": "you are a expert in writing an email, whatever kind of email it is, you can write it in a professional way and make it look good and original giving it a little human touch.",
        },
        {
            "role": "user",
            "content": f"I need to write an email of {email_type}",
        }
    ],
)

print(response.content)